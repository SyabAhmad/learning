"""
Backend System Entry Point.
Initializes environment and runs the backend system.
"""

# Standard library imports
import os


# Third-party imports
from dotenv import load_dotenv
from flask import Flask
import routs

from routs.upload import toUpload

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.register_blueprint(routs.upload_blueprint, url_prefix='/api')

if __name__ == "__main__":
    print("Application is running...")
    print(toUpload())  # This will now work for direct testing
    # app.run(debug=True)