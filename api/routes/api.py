"""
API Routes Configuration.
Handles data processing and secure endpoints for the system.
"""

# Third-party imports
from flask import jsonify, request
from flask_cors import cross_origin

# Local module imports
from . import api_blueprint

@api_blueprint.route('/data', methods=['GET'])
@cross_origin()  # Enable CORS for this specific route
def get_data():
    """API endpoint with CORS enabled"""
    return jsonify({
        'message': 'CORS-enabled API endpoint',
        'data': ['item1', 'item2', 'item3']
    })

@api_blueprint.route('/secure', methods=['POST'])
@cross_origin(origins=['https://trusted-domain.com'])
def secure_endpoint():
    """Secure endpoint with restricted CORS"""
    data = request.get_json()
    return jsonify({
        'received': data,
        'status': 'processed'
    })