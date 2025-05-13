# from flask import Flask
# from app.api.routes import quote_api

# def create_app():
#     app = Flask(__name__)
#     app.register_blueprint(quote_api)
#     return app

from flask import Flask, render_template
from app.api.routes import quote_api

def create_app():
    app = Flask(__name__)
    app.register_blueprint(quote_api)

    # Route for frontend
    @app.route('/')
    def index():
        return render_template('index.html')

    return app
