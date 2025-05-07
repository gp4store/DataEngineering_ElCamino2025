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

def create_firehose_delivery_stream(firehose_name, s3_bucket, data_stream_name, region=None, role_arn=None):
    """
    Create a Kinesis Firehose delivery stream with a Kinesis Data Stream as source
    
    :param firehose_name: Name of the Firehose delivery stream to create
    :param s3_bucket: S3 bucket name for destination
    :param data_stream_name: Source Kinesis Data Stream name
    :param region: AWS region for the Firehose (default: None, uses default region)
    :param role_arn: IAM Role ARN for Firehose permissions
    :return: Response from AWS API if successful, None otherwise
    """
    # Validate required parameters
    if not firehose_name or not s3_bucket or not data_stream_name:
        print("Error: firehose_name, s3_bucket, and data_stream_name are required")
        return None
        
    # Get account ID from STS if not provided
    try:
        firehose_client = boto3.client('firehose', region_name=region)
        sts_client = boto3.client('sts')
        account_id = sts_client.get_caller_identity()['Account']
        
        # Use provided role ARN or create a default value
        if not role_arn:
            role_arn = f'arn:aws:iam::{account_id}:role/firehose-role'
            print(f"No role_arn provided, using default: {role_arn}")
        
        # Create the region string
        region_str = region if region else boto3.session.Session().region_name
        if not region_str:
            region_str = 'us-west-1'  # Default fallback
            
        response = firehose_client.create_delivery_stream(
            DeliveryStreamName=firehose_name,
            DeliveryStreamType='KinesisStreamAsSource',
            KinesisStreamSourceConfiguration={
                'KinesisStreamARN': f'arn:aws:kinesis:{region_str}:{account_id}:stream/{data_stream_name}',
                'RoleARN': role_arn
            },
            S3DestinationConfiguration={
                'BucketARN': f'arn:aws:s3:::{s3_bucket}',
                'RoleARN': role_arn
            }
        )
        print(f'Delivery Stream {firehose_name} created with ARN: {response["DeliveryStreamARN"]}')
        return response
    except Exception as e:
        print(f"Error creating Kinesis Firehose delivery stream: {e}")
        return None


def wait_for_kinesis_stream_active(stream_name, region=None, timeout_seconds=120):
    """
    Wait for a Kinesis stream to become active before proceeding
    
    :param stream_name: Name of the stream to wait for
    :param region: AWS region of the stream
    :param timeout_seconds: Maximum time to wait in seconds
    :return: True if stream became active, False if timeout or error
    """
    import time
    
    try:
        kinesis_client = boto3.client(
            'kinesis',
            region_name=region if region else 'us-west-1'
        )
        
        print(f"Waiting for Kinesis stream '{stream_name}' to become active...")
        
        # Check stream status in a loop
        start_time = time.time()
        while time.time() - start_time < timeout_seconds:
            response = kinesis_client.describe_stream(StreamName=stream_name)
            status = response['StreamDescription']['StreamStatus']
            
            if status == 'ACTIVE':
                print(f"Stream '{stream_name}' is now active")
                return True
                
            print(f"Stream status: {status}. Waiting...")
            time.sleep(10)  # Wait 10 seconds before checking again
            
        print(f"Timeout waiting for stream '{stream_name}' to become active")
        return False
        
    except Exception as e:
        print(f"Error while waiting for stream: {e}")
        return False


def setup_aws_resources(bucket_name, stream_name, firehose_name=None, region='us-west-1', 
                       shard_count=1, role_arn=None, wait_for_stream=True):
    """
    Set up complete data pipeline with S3 bucket, Kinesis data stream, and Firehose
    
    :param bucket_name: Name of S3 bucket to create
    :param stream_name: Name of Kinesis stream to create
    :param firehose_name: Name of Firehose delivery stream (defaults to stream_name + "-firehose")
    :param region: AWS region for resources
    :param shard_count: Number of shards for Kinesis stream
    :param role_arn: IAM role ARN for Firehose permissions
    :param wait_for_stream: Whether to wait for the Kinesis stream to become active
    :return: Tuple of (bucket_success, stream_response, firehose_response)
    """
    print(f"Setting up complete AWS data pipeline in region {region}...")
    
    # Default firehose name if not provided
    if not firehose_name:
        firehose_name = f"{stream_name}-firehose"
    
    # Create S3 bucket
    bucket_success = create_s3_bucket(bucket_name, region)
    if not bucket_success:
        print("Failed to create S3 bucket, aborting pipeline setup")
        return (False, None, None)
    
    # Create Kinesis stream
    stream_response = create_kinesis_stream(stream_name, shard_count, region)
    if not stream_response:
        print("Failed to create Kinesis stream, aborting pipeline setup")
        return (bucket_success, None, None)
    
    # Wait for Kinesis stream to become active if requested
    if wait_for_stream:
        stream_active = wait_for_kinesis_stream_active(stream_name, region)
        if not stream_active:
            print("Kinesis stream did not become active in time, proceeding anyway but Firehose creation might fail")
    
    # Create Firehose delivery stream to connect Kinesis to S3
    firehose_response = create_firehose_delivery_stream(
        firehose_name, 
        bucket_name, 
        stream_name,
        region,
        role_arn
    )
    
    return (bucket_success, stream_response, firehose_response)

# Example usage
if __name__ == "__main__":
    # Configuration
    BUCKET_NAME = "de-week16-bucket"
    STREAM_NAME = "de-week16-stream"
    FIREHOSE_NAME = "de-week16-firehose"
    REGION = "us-west-1"
    SHARD_COUNT = 1
    
    # Setup complete data pipeline
    bucket_result, stream_result, firehose_result = setup_aws_resources(
        BUCKET_NAME, 
        STREAM_NAME,
        FIREHOSE_NAME,
        REGION,
        SHARD_COUNT
    )
    
    # Final status report
    if bucket_result and stream_result and firehose_result:
        print(f"Successfully created complete data pipeline:")
        print(f"- S3 Bucket: {BUCKET_NAME}")
        print(f"- Kinesis Stream: {STREAM_NAME} with {SHARD_COUNT} shard(s)")
        print(f"- Firehose Delivery Stream: {FIREHOSE_NAME}")
    else:
        print("There were errors creating the AWS resources. Check the logs above.")