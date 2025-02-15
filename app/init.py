# Ensure all imports are at the top of the file
import app.routes

# Create application factory function
from flask import Flask

def create_app():
    app = Flask(__name__)
    with app.app_context():
        # Include routes from the routes module
        from . import routes
    return app
