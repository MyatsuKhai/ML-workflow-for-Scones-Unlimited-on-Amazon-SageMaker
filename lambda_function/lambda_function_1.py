import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    key = event["s3_key"]
    bucket = event["s3_bucket"]
    file_name = '/tmp/image.png'
    s3.download_file(bucket,key,file_name)
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())
    # print("Event:",event.keys())
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket" : bucket,
            "s3_key" : key,
            "inferences":[]
        }
    }