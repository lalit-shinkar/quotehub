from flask import Blueprint, jsonify
import random

quote_api = Blueprint('quote_api', __name__)

QUOTES = [
    "Stay hungry. Stay foolish.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "Simplicity is the soul of efficiency.",
    "First, solve the problem. Then, write the code."
]

@quote_api.route('/api/quote')
def get_quote():
    return jsonify({"quote": random.choice(QUOTES)})

