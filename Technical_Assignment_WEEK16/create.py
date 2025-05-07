#!/usr/bin/python3

import boto3

def create_s3_bucket(bucket_name, region=None):
    """
    Create an S3 bucket in a specified region
    
    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-1'
    :return: True if bucket created, else False
    """
    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration=location
            )
        print(f"S3 bucket {bucket_name} created successfully")
        return True
    except Exception as e:
        print(f"Error creating bucket: {e}")
        return False

def create_kinesis_stream(stream_name, shard_count=1, region=None):
    """
    Create a Kinesis data stream
    
    :param stream_name: Name of the stream to create
    :param shard_count: Number of shards for the stream
    :param region: AWS region to create the stream in
    :return: Response from AWS API if successful, None otherwise
    """
    try:
        # Create kinesis client with specified region
        kinesis_client = boto3.client(
            'kinesis',
            region_name=region if region else 'us-west-1'
        )
        
        # Create the Kinesis Data Stream
        response = kinesis_client.create_stream(
            StreamName=stream_name,
            ShardCount=shard_count
        )
        
        print(f"Kinesis data stream '{stream_name}' created successfully")
        return response
    except Exception as e:
        print(f"Error creating Kinesis stream: {e}")
        return None

def setup_aws_resources(bucket_name, stream_name, region='us-west-1', shard_count=1):
    """
    Set up both S3 bucket and Kinesis data stream
    
    :param bucket_name: Name of S3 bucket to create
    :param stream_name: Name of Kinesis stream to create
    :param region: AWS region for resources
    :param shard_count: Number of shards for Kinesis stream
    :return: Tuple of (bucket_success, stream_response)
    """
    print(f"Setting up AWS resources in region {region}...")
    
    # Create S3 bucket
    bucket_success = create_s3_bucket(bucket_name, region)
    
    # Create Kinesis stream
    stream_response = create_kinesis_stream(stream_name, shard_count, region)
    
    return (bucket_success, stream_response)

# Example usage
if __name__ == "__main__":
    # Configuration
    BUCKET_NAME = "my-data-bucket"
    STREAM_NAME = "my-data-stream"
    REGION = "us-west-1"
    SHARD_COUNT = 1
    
    # Setup both resources
    bucket_result, stream_result = setup_aws_resources(
        BUCKET_NAME, 
        STREAM_NAME,
        REGION,
        SHARD_COUNT
    )
    
    # Final status report
    if bucket_result and stream_result:
        print(f"Successfully created all AWS resources:")
        print(f"- S3 Bucket: {BUCKET_NAME}")
        print(f"- Kinesis Stream: {STREAM_NAME} with {SHARD_COUNT} shard(s)")
    else:
        print("There were errors creating the AWS resources. Check the logs above.")