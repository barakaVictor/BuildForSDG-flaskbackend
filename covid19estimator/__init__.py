import logging
import time
from flask import Flask, g, request
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

    @app.before_request
    def start_request_timer():
        g.start = time.time()

    @app.after_request
    def log_request_info(response):
        if request.path in app.config.get("LOG_ROUTES"):
            diff = "{:02}".format(int((time.time() - g.start) * 1000))
            log = f"{request.method} {request.path} {response.status_code} {diff}ms"
            app.logger.info(log)
        return response

    return app