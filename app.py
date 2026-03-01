from flask import Flask, request, jsonify
from flatlib.chart import Chart
from flatlib import const
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
import random

app = Flask(__name__)

def creer_theme(date, heure, latitude, longitude):
    dt = Datetime(date, heure, '+00:00')
    pos = GeoPos(latitude, longitude)
    chart = Chart(dt, pos)

    theme = {
        'soleil': chart.get(const.SUN).sign,
        'lune': chart.get(const.MOON).sign,
        'ascendant': chart.get(const.ASC).sign,
    }
    return theme

def compatibilite(theme1, theme2):
    score = 0
    total = 30

    if theme1['soleil'] == theme2['soleil']:
        score += 10
    if theme1['lune'] == theme2['lune']:
        score += 10
    if theme1['ascendant'] == theme2['ascendant']:
        score += 10

    return round((score / total) * 100, 1)

@app.route('/compatibilite', methods=['POST'])
def calcul_compatibilite():
    data = request.json

    theme1 = creer_theme(
        data['date1'],
        data['heure1'],
        data['lat1'],
        data['lon1']
    )

    theme2 = creer_theme(
        data['date2'],
        data['heure2'],
        data['lat2'],
        data['lon2']
    )

    score = compatibilite(theme1, theme2)

    return jsonify({
        "compatibilite": score,
        "theme1": theme1,
        "theme2": theme2
    })

if __name__ == '__main__':
    app.run()
