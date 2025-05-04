#!/usr/bin/python3

import boto3

def create_s3_bucket(bucket_name, region=None):
    """
    Create an S3 bucket in a specified region
    
    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
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

# Example usage
if __name__ == "__main__":
    bucket_name = "de-week16-gp-bucket"
    region = "us-west-1"
    create_s3_bucket(bucket_name, region)