import boto3


def getS3Client():
    client = boto3.client(
        "s3",

    )