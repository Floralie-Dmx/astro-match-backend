from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/inscription", methods=["POST"])
def inscription():
    # Récupération des données envoyées par Lovable
    data = request.get_json()
    prenom = data.get("prenom")
    email = data.get("email")
    mot_de_passe = data.get("mot_de_passe")
    date_heure_naissance = data.get("date_heure_naissance")
    ville_naissance = data.get("ville_naissance")

    # Vérification que tous les champs sont présents
    if not all([prenom, email, mot_de_passe, date_heure_naissance, ville_naissance]):
        return jsonify({"erreur": "Champs manquants"}), 400

    # Ici tu peux mettre le calcul astrologique (exemple fictif)
    return jsonify({
        "soleil": "Taureau",
        "lune": "Cancer",
        "ascendant": "Gémeaux",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "compatibilite": 87
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
