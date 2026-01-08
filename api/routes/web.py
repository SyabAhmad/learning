"""
Web Routes Configuration.
Serves the HTML frontend and informational pages.
"""

# Third-party imports
from flask import render_template

# Local module imports
from . import web_blueprint

@web_blueprint.route('/')
def index():
    """Main web page"""
    return render_template('index.html')

@web_blueprint.route('/about')
def about():
    """About page"""
    return "About Flask CORS Demo"