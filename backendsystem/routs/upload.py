from flask import Blueprint, request, jsonify
from config.db import get_s3_client
import os

upload_blueprint = Blueprint('upload', __name__)

def upload_file_logic(file_obj=None, filename=None):
    s3_client = get_s3_client()
    bucket_name = os.getenv('AWS_S3_BUCKET')
    if not bucket_name:
        return {'status': 'error', 'error': 'AWS_S3_BUCKET not set in environment'}
    if file_obj and filename:
        try:
            s3_client.upload_fileobj(file_obj, bucket_name, filename)
            return {'status': 'success', 'filename': filename}
        except Exception as e:
            return {'status': 'error', 'error': str(e)}
    else:
        # If no file provided, just test connection
        try:
            buckets = s3_client.list_buckets()
            bucket_names = [b['Name'] for b in buckets.get('Buckets', [])]
            return {'status': 'success', 'buckets': bucket_names}
        except Exception as e:
            return {'status': 'error', 'error': str(e)}

@upload_blueprint.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'status': 'error', 'error': 'No file part in request'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'status': 'error', 'error': 'No selected file'}), 400
    result = upload_file_logic(file, file.filename)
    return jsonify(result)

def toUpload():
    # For direct testing, just list buckets (no file upload)
    return upload_file_logic()