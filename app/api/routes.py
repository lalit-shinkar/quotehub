# from flask import Blueprint, jsonify
# import random

# quote_api = Blueprint('quote_api', __name__)

# QUOTES = [
#     "Stay hungry. Stay foolish.",
#     "Code is like humor. When you have to explain it, it’s bad.",
#     "Simplicity is the soul of efficiency.",
#     "First, solve the problem. Then, write the code."
# ]

# @quote_api.route('/api/quote')
# def get_quote():
#     return jsonify({"quote": random.choice(QUOTES)})

from flask import Flask
from routes import quote_api  # Import the blueprint

def create_app():
    app = Flask(__name__)

    # Register the Blueprint
    app.register_blueprint(quote_api)

    # Add the root route
    @app.route('/')
    def home():
        return 'Welcome to the QuoteHub API!'

    return app
