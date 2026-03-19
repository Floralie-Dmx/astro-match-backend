from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulation base de données en mémoire
users_db = {}

@app.route("/")
def home():
    return "Cosmos API en ligne 🚀"

# Inscription
@app.route("/inscription", methods=["POST"])
def inscription():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Aucune donnée reçue"}), 400

    # Champs obligatoires
    required_fields = ["prenom", "email", "mot_de_passe", "date_heure_naissance", "ville_naissance", "consentement"]
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"error": f"Champ manquant ou vide: {field}"}), 400

    # Vérifier consentement RGPD
    if data["consentement"] != True:
        return jsonify({"error": "Consentement obligatoire"}), 403

    email = data["email"]
    if email in users_db:
        return jsonify({"error": "Utilisateur déjà existant"}), 400

    # Enregistrer l’utilisateur
    users_db[email] = {
        "prenom": data["prenom"],
        "mot_de_passe": data["mot_de_passe"],
        "date_heure_naissance": data["date_heure_naissance"],
        "ville_naissance": data["ville_naissance"]
    }

    # ⚡ Simulation calcul astrologique
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
            "prenom": data["prenom"],
            "email": email,
            "soleil": soleil,
            "lune": lune,
            "ascendant": ascendant,
            "latitude": latitude,
            "longitude": longitude,
            "compatibilite": compatibilite
        }
    })

# Consultation de ses données
@app.route("/mes_donnees", methods=["POST"])
def mes_donnees():
    data = request.get_json()
    email = data.get("email")
    mot_de_passe = data.get("mot_de_passe")
    if not email or not mot_de_passe:
        return jsonify({"error": "Email et mot de passe obligatoires"}), 400

    user = users_db.get(email)
    if not user or user["mot_de_passe"] != mot_de_passe:
        return jsonify({"error": "Utilisateur non trouvé ou mot de passe incorrect"}), 403

    return jsonify({"success": True, "data": user})

# Suppression de compte
@app.route("/supprimer_compte", methods=["POST"])
def supprimer_compte():
    data = request.get_json()
    email = data.get("email")
    mot_de_passe = data.get("mot_de_passe")
    if not email or not mot_de_passe:
        return jsonify({"error": "Email et mot de passe obligatoires"}), 400

    user = users_db.get(email)
    if not user or user["mot_de_passe"] != mot_de_passe:
        return jsonify({"error": "Utilisateur non trouvé ou mot de passe incorrect"}), 403

    del users_db[email]
    return jsonify({"success": True, "message": "Compte supprimé avec succès"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
