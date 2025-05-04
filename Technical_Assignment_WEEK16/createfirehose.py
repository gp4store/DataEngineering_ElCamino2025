import boto3
import json

def create_firehose_delivery_stream(kinesis_stream_name, s3_bucket_name, delivery_stream_name):
    # Create a Firehose client
    firehose_client = boto3.client('firehose')
    
    # Create the Firehose delivery stream
    response = firehose_client.create_delivery_stream(
        DeliveryStreamName=delivery_stream_name,
        DeliveryStreamType='KinesisStreamAsSource',
        KinesisStreamSourceConfiguration={
            'KinesisStreamARN': f'arn:aws:kinesis:us-east-1:{get_account_id()}:{kinesis_stream_name}',
            'RoleARN': f'arn:aws:iam::{get_account_id()}:role/de-kinesis'
        },
        S3DestinationConfiguration={
            'RoleARN': f'arn:aws:iam::{get_account_id()}:role/de-kinesis',
            'BucketARN': f'arn:aws:s3:::{s3_bucket_name}',
            'BufferingHints': {
                'SizeInMBs': 5,
                'IntervalInSeconds': 300
            },
            'CompressionFormat': 'UNCOMPRESSED',
            'Prefix': 'kinesis-data/',
            'ErrorOutputPrefix': 'error/'
        }
    )
    
    return response

def get_account_id():
    # Get the AWS account ID
    sts_client = boto3.client('sts')
    return sts_client.get_caller_identity()['Account']

if __name__ == "__main__":
    # Replace with your actual resource names
    kinesis_stream_name = "de-week16-stream"
    s3_bucket_name = "de-week16-gp-bucket"
    delivery_stream_name = "de-week16-gp-delivery-stream"
    
    response = create_firehose_delivery_stream(kinesis_stream_name, s3_bucket_name, delivery_stream_name)
    print(f"Delivery stream created: {json.dumps(response, indent=2)}")