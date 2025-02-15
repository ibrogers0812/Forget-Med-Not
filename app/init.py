# app/__init__.py

from flask import Flask

app = Flask(__name__)

from app import routes  # Import routes to register the endpoints

def create_app():
    app.config['SECRET_KEY'] = 'your_secret_key'
    # Add other configurations here
    return app
