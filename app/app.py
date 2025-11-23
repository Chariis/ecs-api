import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = os.environ.get('APP_VERSION', '1.0')

@app.route('/')
def home():
    """Serves the main page, showing the app version."""
    return f"<h1>Hello, World!</h1><h2>Version: {APP_VERSION}</h2>"

@app.route('/health')
def health_check():
    """Serves a health check endpoint for the load balancer."""
    return jsonify({"status": "healthy", "version": APP_VERSION}), 200

if __name__ == "__main__":
    # Run on 0.0.0.0 to be accessible outside the container
    app.run(host='0.0.0.0', port=5000)