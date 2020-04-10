import logging
import time
from flask import g, request
from covid19estimator import create_app

app = create_app()
 
@app.before_request
def start_request_timer():
    g.start = time.time()

@app.after_request
def log_request_info(response):
    if request.path in app.config.get("LOG_ROUTES"):
        diff = int((time.time() - g.start) * 1000)
        log = f"{request.method} {request.path} {response.status_code} {diff} ms"
        app.logger.info(log)
    return response

if __name__ == "__main__":
    app.run()
