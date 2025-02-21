from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

import os
from src.integration_config import SPECIFICATION

load_dotenv()

app = Flask(__name__)
app.config['ENV'] = os.getenv('FLASK_ENV', "production")
app.config['DEBUG'] = os.getenv('FLASK_DEBUG', "0") == "1"


CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=False)

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "message": "Not Found",
        "status": 404,
        "endpoint": "https://devbot-integration-spec.up.railway.app/api/integration.json"
    }), 404

@app.route('/api/integration.json')
def get_integration_spec():
    return jsonify(SPECIFICATION)

