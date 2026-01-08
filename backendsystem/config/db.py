"""
Database and Storage Configuration.
Initializes connections to external services like AWS S3 or PostgreSQL.
"""

# Standard library imports
import os

# Third-party imports
import boto3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_s3_client():
    """
    Creates and returns an AWS S3 client using environment credentials.
    
    Returns:
        boto3.client: An initialized S3 client instance.
    """
    client = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("S3_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("S3_SECRET_ACCESS_KEY"),
        region_name=os.getenv("S3_REGION", "ap-southeast-4")
    )
    return client

if __name__ == "__main__":
    # Test connection if run directly
    try:
        s3 = get_s3_client()
        print("S3 Client initialized successfully.")
    except Exception as e:
        print(f"Failed to initialize S3 client: {e}")