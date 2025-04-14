from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

# Chemin vers le fichier JSON
json_path = os.path.join(os.path.dirname(__file__), 'data.json')

@app.route('/')
def home():
    return """
    <h1>Service de logs utilisateurs</h1>
    <p>Accédez aux logs via <a href="/logs">/logs</a></p>
    """

@app.route('/logs')
def get_logs():
    with open(json_path, 'r') as file:
        logs = json.load(file)
    return jsonify(logs)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)