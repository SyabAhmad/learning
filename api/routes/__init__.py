from flask import Blueprint

# Create blueprints
api_blueprint = Blueprint('api', __name__)
web_blueprint = Blueprint('web', __name__)

# Import routes to register them
from . import api, web