from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Load configurations
    app.config.from_pyfile('config.py')

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Import and register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
