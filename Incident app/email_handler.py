import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, recipient_emails):
     # Securely retrieve credentials from environment variables
     sender_email = os.getenv("EMAIL_USER")
     sender_password = os.getenv("EMAIL_PASS")

     # Prepare email
     msg = MIMEMultipart()
     msg["From"] = sender_email
     msg["Subject"] = subject

     # Handle multiple recipients
     if isinstance(recipient_emails, list):
         msg["To"] = ", ".join(recipient_emails)
     else:
         msg["To"] = recipient_emails

     msg.attach(MIMEText(body, "plain"))

     try:
         with smtplib.SMTP("smtp.gmail.com", 587) as server:
             server.starttls()  # Secure the connection
             server.login(sender_email, sender_password)
             server.sendmail(sender_email, recipient_emails, msg.as_string())
         print("Email sent successfully!")
     except Exception as e:
         print(f"Failed to send email: {e}")