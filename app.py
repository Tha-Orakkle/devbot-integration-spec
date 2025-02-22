from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

import os
from src.integration_config import SPECIFICATION

load_dotenv()

app = Flask(__name__, static_folder='images')
app.config['ENV'] = os.getenv('FLASK_ENV', "production")
app.config['DEBUG'] = os.getenv('FLASK_DEBUG', "0") == "1"

CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=False)

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "message": "Not Found",
        "status": 404,
        "specification_url": "https://devbot-integration-spec.up.railway.app/v1/integration.json"
    }), 404

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "message": "welcome to devbot integration specification",
        "specification_url": "https://devbot-integration-spec.up.railway.app/v1/integration.json" 
    })

@app.route('/v1/integration.json', methods=['GET'])
def get_integration_spec():
    return jsonify(SPECIFICATION)


@app.route('/v1/devbot-logo.jpg', methods=['GET'])
def app_logo():
    return app.send_static_file('devbot.jpg')