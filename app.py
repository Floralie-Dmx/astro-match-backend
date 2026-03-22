from flask import Flask, request, jsonify

app = Flask(__name__)

users_db = {}

@app.route("/")
def home():
    return "CosmoHeart API en ligne 🚀"

# INSCRIPTION
@app.route("/inscription", methods=["POST"])
def inscription():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON manquant"}), 400

    required_fields = [
        "prenom",
        "email",
        "mot_de_passe",
        "date_heure_naissance",
        "ville_naissance",
        "latitude",
        "longitude",
        "consentement"
    ]

    for field in required_fields:
        if field not in data or data[field] in [None, ""]:
            return jsonify({"error": f"Champ manquant : {field}"}), 400

    if data["consentement"] != True:
        return jsonify({"error": "Consentement requis"}), 403

    email = data["email"]

    if email in users_db:
        return jsonify({"error": "Utilisateur déjà existant"}), 400

    users_db[email] = {
        "prenom": data["prenom"],
        "mot_de_passe": data["mot_de_passe"],
        "date_heure_naissance": data["date_heure_naissance"],
        "ville_naissance": data["ville_naissance"],
        "latitude": data["latitude"],
        "longitude": data["longitude"]
    }

    return jsonify({
        "success": True,
        "data": {
            "prenom": data["prenom"],
            "email": email,
            "soleil": "Balance",
            "lune": "Cancer",
            "ascendant": "Lion",
            "compatibilite": 80
        }
    })


# CONNEXION (SÉCURISÉE)
@app.route("/mes_donnees", methods=["POST"])
def mes_donnees():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON manquant"}), 400

    email = data.get("email")
    password = data.get("mot_de_passe")

    user = users_db.get(email)

    if not user or user["mot_de_passe"] != password:
        return jsonify({"error": "Identifiants incorrects"}), 403

    # 🔐 VERSION SÉCURISÉE (sans mot de passe)
    user_safe = {
        "prenom": user["prenom"],
        "date_heure_naissance": user["date_heure_naissance"],
        "ville_naissance": user["ville_naissance"],
        "latitude": user["latitude"],
        "longitude": user["longitude"]
    }

    return jsonify({
        "success": True,
        "data": user_safe
    })


# SUPPRESSION
@app.route("/supprimer_compte", methods=["POST"])
def supprimer_compte():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON manquant"}), 400

    email = data.get("email")
    password = data.get("mot_de_passe")

    user = users_db.get(email)

    if not user or user["mot_de_passe"] != password:
        return jsonify({"error": "Accès refusé"}), 403

    del users_db[email]

    return jsonify({
        "success": True,
        "message": "Compte supprimé"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
