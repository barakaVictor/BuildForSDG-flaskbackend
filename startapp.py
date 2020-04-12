"""
The purpose of this script is to launch the
application in development mode. It should not
be used launch the application in any production
environment
"""
from covid19estimator import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
