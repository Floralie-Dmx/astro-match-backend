from flask import Flask, request, jsonify
from datetime import datetime
import random

app = Flask(__name__)

# Fonction astrologique simplifiée
def calcul_astrologie(birth_datetime, birth_city):
    # Exemple simplifié : tu remplaceras par ton vrai calcul
    soleil = "Lion"
    lune = "Cancer"
    ascendant = "Balance"
    latitude = 48.8566  # Exemple : Paris
    longitude = 2.3522
    compatibilite = random.randint(50, 100)
    return soleil, lune, ascendant, latitude, longitude, compatibilite

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

        # Calcul astrologique
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
