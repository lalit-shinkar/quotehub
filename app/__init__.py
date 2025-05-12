from flask import Flask
from app.api.routes import quote_api

def create_app():
    app = Flask(__name__)
    app.register_blueprint(quote_api)
    return app

