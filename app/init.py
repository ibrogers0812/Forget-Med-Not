from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from models import User  # Ensure 'User' is imported before use

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Configure login manager
    login_manager.login_view = 'auth.login'

    # Register blueprints
    from route import main
    app.register_blueprint(main)

    # Additional setup, e.g., database migrations

    return app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))