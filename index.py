from flask import Flask, jsonify
import datetime
import random
import os  # Ajout de cette importation

app = Flask(__name__)

# Générer des logs utilisateurs simulés
def generate_user_logs(n=50):
    logs = []
    actions = ["login", "logout", "view_page", "click_button", "submit_form", "download", "upload"]
    pages = ["accueil", "profil", "paramètres", "produits", "contact", "aide", "blog"]
    statuses = ["success", "error", "warning", "info"]
    
    # Date de début (il y a 7 jours)
    start_date = datetime.datetime.now() - datetime.timedelta(days=7)
    
    for i in range(n):
        user_id = random.randint(1, 100)
        action = random.choice(actions)
        page = random.choice(pages)
        status = random.choice(statuses)
        
        # Générer un timestamp aléatoire dans les 7 derniers jours
        random_seconds = random.randint(0, 7 * 24 * 60 * 60)
        timestamp = start_date + datetime.timedelta(seconds=random_seconds)
        
        logs.append({
            "id": i + 1,
            "user_id": user_id,
            "action": action,
            "page": page,
            "status": status,
            "timestamp": timestamp.isoformat(),
            "ip_address": f"192.168.{random.randint(1, 255)}.{random.randint(1, 255)}"
        })
    
    return logs

# Route pour servir les logs en JSON
@app.route('/api/logs', methods=['GET'])
def get_logs():
    logs = generate_user_logs()
    return jsonify(logs)

# Route racine
@app.route('/')
def index():
    return """
    <html>
        <head>
            <title>Service de Logs</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }
                h1 { color: #333; }
                .container { max-width: 800px; margin: 0 auto; }
                code { background: #f4f4f4; padding: 2px 5px; border-radius: 3px; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Service de Logs Utilisateurs</h1>
                <p>Bienvenue sur le service de logs utilisateurs simulés.</p>
                <p>Pour accéder aux logs, utilisez l'URL: <code>/api/logs</code></p>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))