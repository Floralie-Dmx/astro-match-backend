from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()  # récupère le JSON envoyé par Lovable
    prenom = data.get("prenom")
    email = data.get("email")
    password = data.get("password")
    birthDateTime = data.get("birthDateTime")
    birthCity = data.get("birthCity")

    # Si un champ manque → erreur 400
    if not all([prenom, email, password, birthDateTime, birthCity]):
        return jsonify({"error": "Champs manquants"}), 400

    # Calcul astrologique fictif pour tester
    return jsonify({
        "soleil": "Taureau",
        "lune": "Cancer",
        "ascendant": "Gémeaux",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "compatibilite": 87
    })
