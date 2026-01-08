"""
Flask Application Entry Point.
Initializes the Flask app, configures CORS, and registers blueprints.
"""

# Third-party imports
from flask import Flask
from flask_cors import CORS

# Local module imports
from config import Config
from routes.api import api_blueprint
from routes.web import web_blueprint

def create_app():
    """
    Application factory pattern to create and configure the Flask app.
    
    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize CORS
    CORS(app, resources={
        r"/api/*": {
            "origins": ["http://localhost:3000", "https://example.com"],
            "methods": ["GET", "POST", "PUT", "DELETE"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })

    # Register blueprints
    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.register_blueprint(web_blueprint)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)