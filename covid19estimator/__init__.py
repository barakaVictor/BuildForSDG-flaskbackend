from flask import Flask
from flask_cors import CORS

def create_app(config='covid19estimator.settings'):
    app = Flask(__name__)
    app.config.from_object(config)
    CORS(app, resources=app.config.get("ALLOWED_ORIGINS"))

    #Registering views for the app
    from .api import api_bp
    app.register_blueprint(api_bp)

    from .main import main_bp
    app.register_blueprint(main_bp)

    return app