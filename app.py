from flask import Flask, request, jsonify
from datetime import datetime
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
import pyswisseph as swe
import random

app = Flask(__name__)

# Fonction pour générer la latitude/longitude approximative depuis la ville
# Ici un exemple simple : tu peux remplacer par une vraie API géocoding si tu veux
def geocode_city(city_name):
    # Exemple : Paris
    if city_name.lower() == "paris":
        return 48.8566, 2.3522
    # Tu peux ajouter d'autres villes
    return 0.0, 0.0  # Valeur par défaut

# Calcul astrologique avec Flatlib
def calcul_astrologie(birth_datetime, birth_city):
    lat, lon = geocode_city(birth_city)
    pos = GeoPos(lat, lon)
    dt = Datetime(birth_datetime.year, birth_datetime.month, birth_datetime.day,
                  birth_datetime.hour, birth_datetime.minute, 'UTC')
    chart = Chart(dt, pos)
    
    # Récupération des planètes importantes
    soleil = chart.get('SUN').sign
    lune = chart.get('MOON').sign
    ascendant = chart.get('ASC').sign
    
    # Compatibilité fictive pour l’exemple
    compatibilite = random.randint(50, 100)
    
    return soleil, lune, ascendant, lat, lon, compatibilite

@app.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.json
        prenom = data.get('prenom')
        email = data.get('email')
        password = data.get('password')
        birthCity = data.get('birthCity')
        
        birth_datetime_str = data.get('birthDateTime')
        dt = datetime.fromisoformat(birth_datetime_str.replace("Z", ""))
        date_of_birth = dt.date()
        time_of_birth = dt.time()
        
        soleil, lune, ascendant, latitude, longitude, compatibilite = calcul_astrologie(dt, birthCity)
        
        user_data = {
            "prenom": prenom,
            "email": email,
            "password": password,
            "birthCity": birthCity,
            "dateOfBirth": str(date_of_birth),
            "timeOfBirth": str(time_of_birth),
            "soleil": soleil,
            "lune": lune,
            "ascendant": ascendant,
            "latitude": latitude,
            "longitude": longitude,
            "compatibilite": compatibilite
        }
        
        return jsonify({"success": True, "user": user_data})
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
