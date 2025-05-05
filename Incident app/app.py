from flask import Flask, request, render_template
from email_handler import send_email
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')  # Replace with your database file
    conn.row_factory = sqlite3.Row
    return conn

# Home route
@app.route('/')
def home():
    return render_template('home.html')  # Render the vibrant homepage

# Create incident route
@app.route('/create_incident', methods=['POST'])
def create_incident():
    title = request.form['title']
    description = request.form['description']

    # Save to database
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO incidents (title, description) VALUES (?, ?)',
        (title, description)
    )
    conn.commit()
    conn.close()

    # Send email notification
    subject = f"New Incident Created: {title}"
    body = f"Details:\nTitle: {title}\nDescription: {description}"
    recipient_emails = ["recipient1@example.com", "recipient2@example.com"]
    send_email(subject, body, recipient_emails)

    return "Incident created and email notification sent!"

# Run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)