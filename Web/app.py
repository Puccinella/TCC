import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from flask import Flask, jsonify, render_template
from banco_de_dados import conectar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('teste.html')

@app.route('/api/log')
def get_log():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.prontuario, l.status, l.data_hora
        FROM log l
        JOIN pessoas p ON p.id = l.pessoa_id
        ORDER BY l.data_hora DESC
    """)
    linhas = cursor.fetchall()
    cursor.close()
    conn.close()

    log = []
    for i, (prontuario, status, data_hora) in enumerate(linhas, start=1):
        log.append({
            "numero": i,
            "prontuario": prontuario,
            "status": status,
            "data_hora": data_hora.isoformat()
        })

    return jsonify(log)


if __name__ == "__main__":
    app.run(debug=True)