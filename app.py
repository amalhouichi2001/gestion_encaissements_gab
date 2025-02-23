from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)  # Autorise les requêtes cross-origin

def get_encaissements():
    try:
        conn = psycopg2.connect(
            dbname="gestion_encaissements",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM encaissements;")
        rows = cursor.fetchall()
        conn.close()
        
        data = [
            {"id": row[0], "date_encaissement": row[1], "montant": row[2], "moyen_paiement": row[3]}
            for row in rows
        ]
        
        print("Données récupérées :", data)  # Affiche les données dans le terminal
        return data
    except Exception as e:
        print("Erreur lors de la récupération des encaissements :", e)
        return []

@app.route('/api/encaissements', methods=['GET'])
def api_encaissements():
    return jsonify(get_encaissements())

if __name__ == '__main__':
    app.run(debug=True)
