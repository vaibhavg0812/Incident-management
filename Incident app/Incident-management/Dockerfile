# Use an updated lightweight Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies (optional, good for emails, SQLite, etc.)
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Copy only requirements first (Docker caching best practice)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the project
COPY . .

# Expose the port that Flask uses
EXPOSE 5000

# Define environment variable for Flask
ENV FLASK_APP=app.py

# Command to run the application
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]

