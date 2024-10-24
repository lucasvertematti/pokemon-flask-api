from flask import Flask
from .config import Config
from .auth import auth
from .routes import api_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register Blueprints
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(api_routes, url_prefix='/api')

    return app
