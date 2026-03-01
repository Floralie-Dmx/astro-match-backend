from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Exemple de fonction astrologique simplifiée
def calcul_compatibilite(user_data):
    # Ici tu mets ton vrai calcul astrologique avec flatlib ou autre
    # Pour l'exemple, on renvoie un score aléatoire
    import random
    return random.randint(50, 100)  # Pourcentage de compatibilité

@app.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.json

        # Récupération des champs envoyés par Adalo
        prenom = data.get('prenom')
        email = data.get('email')
        password = data.get('password')
        birthCity = data.get('birthCity')

        # Date + heure de naissance
        birth_datetime_str = data.get('birthDateTime')  # Ex : 1995-08-14T14:30:00.000Z
        dt = datetime.fromisoformat(birth_datetime_str.replace("Z", ""))
        date_of_birth = dt.date()
        time_of_birth = dt.time()

        # Préparer les données utilisateur
        user_data = {
            "prenom": prenom,
            "email": email,
            "password": password,
            "birthCity": birthCity,
            "dateOfBirth": str(date_of_birth),
            "timeOfBirth": str(time_of_birth)
        }

        # Calcul de compatibilité (exemple)
        compatibilite = calcul_compatibilite(user_data)
        user_data['compatibilite'] = compatibilite

        # Ici tu peux enregistrer user_data dans ta base si besoin
        # Exemple : MongoDB, PostgreSQL, Firebase, etc.

        return jsonify({"success": True, "user": user_data})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

# Point d'entrée pour Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)z
