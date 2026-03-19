from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Cosmos API en ligne 🚀"

@app.route("/inscription", methods=["POST"])
def inscription():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Aucune donnée reçue"}), 400

    required_fields = [
        "prenom",
        "email",
        "mot_de_passe",
        "date_heure_naissance",
        "ville_naissance"
    ]

    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"error": f"Champ manquant ou vide: {field}"}), 400

    prenom = data["prenom"]
    email = data["email"]
    date_naissance = data["date_heure_naissance"]
    ville = data["ville_naissance"]

    # ⚡ Simulation temporaire (structure prête pour vrai calcul plus tard)
    soleil = "Balance"
    lune = "Cancer"
    ascendant = "Lion"

    latitude = 48.8566
    longitude = 2.3522

    compatibilite = 75

    return jsonify({
        "success": True,
        "message": "Inscription réussie",
        "data": {
            "prenom": prenom,
            "email": email,
            "soleil": soleil,
            "lune": lune,
            "ascendant": ascendant,
            "latitude": latitude,
            "longitude": longitude,
            "compatibilite": compatibilite
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
