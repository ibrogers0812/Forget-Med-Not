from flask import Flask

def create_app():
    app = Flask(__name__)

    
    # Load configurations from config.py
    app.config.from_pyfile('config.py')

    # Initialize extensions, if any (e.g., database, login manager)
    # db.init_app(app)
    # login_manager.init_app(app)

    # Import and register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
