# Cosmos ❤️ API RGPD Ready

Backend de l'application Cosmos avec respect RGPD.

## Endpoints

### POST /inscription
Données requises:
- prenom
- email
- mot_de_passe
- date_heure_naissance
- ville_naissance
- consentement (true)

### POST /mes_donnees
Consulter ses données:
- email
- mot_de_passe

### POST /supprimer_compte
Supprimer son compte:
- email
- mot_de_passe

## Réponse
- success: True/False
- message: description
- data: informations utilisateur (si applicable)
