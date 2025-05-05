from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('incidents.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('home.html')  # Use the template for the homepage

@app.route('/incidents')
def list_incidents():
    conn = get_db_connection()
    incidents = conn.execute('SELECT * FROM incidents').fetchall()
    conn.close()
    return render_template('incidents.html', incidents=incidents)  # Pass the incidents to the template

if __name__ == '__main__':
    app.run(debug=True)