from flask import Flask, request

app = Flask(__name__)

@app.route('/create_incident', methods=['POST'])
def create_incident():
    title = request.form['title']
    description = request.form['description']

    # Incident creation logic
    return f"Incident '{title}' created successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)