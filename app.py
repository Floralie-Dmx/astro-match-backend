from flask import Flask, request, jsonify

app = Flask(__name__)

users_db = {}

@app.route("/")
def home():
    return "Cosmos API en ligne 🚀"

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
        "date_heure_naissance": data["date_heure_na
