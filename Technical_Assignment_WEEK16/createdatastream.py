#!/usr/bin/python3

import boto3

# Create a boto3 client for Kinesis
# This will automatically use credentials from environment variables,
# AWS config file, or IAM role depending on your environment
kinesis_client = boto3.client(
    'kinesis',
    region_name='us-west-1'  # Specify your desired AWS region
)

# Create a Kinesis Data Stream
response = kinesis_client.create_stream(
    StreamName='my-data-stream',  # Name of your stream
    ShardCount=1  # Number of shards for the stream
)

# Print the response
print(response)