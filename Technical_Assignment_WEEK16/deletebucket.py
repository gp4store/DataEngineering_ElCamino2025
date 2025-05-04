#!/usr/bin/python3

import boto3
from botocore.exceptions import ClientError

def delete_bucket(bucket_name):
    """
    Delete an S3 bucket using boto3 with better error handling.
    
    Args:
        bucket_name (str): Name of the bucket to delete
    """
    # Create S3 resources
    s3_client = boto3.client('s3')
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket(bucket_name)
    
    try:
        # Method 1: Try using resource-based approach first (often works when client operations fail)
        print(f"Attempting to empty and delete bucket {bucket_name}...")
        bucket.objects.all().delete()  # Delete all objects
        
        # Try to delete versioned objects if the bucket is versioned
        try:
            bucket.object_versions.all().delete()  # Delete all versions
        except ClientError as e:
            print(f"Note: Could not delete versions: {e}")
            
        # Now delete the bucket
        bucket.delete()
        print(f"Bucket {bucket_name} has been deleted successfully")
        return True
        
    except ClientError as e:
        print(f"Error using resource-based approach: {e}")
        
        # Method 2: Fall back to a more conservative approach
        print("Trying alternative deletion method...")
        try:
            # List and delete standard objects first
            try:
                paginator = s3_client.get_paginator('list_objects_v2')
                for page in paginator.paginate(Bucket=bucket_name):
                    if 'Contents' in page:
                        delete_keys = {'Objects': [{'Key': obj['Key']} for obj in page['Contents']]}
                        s3_client.delete_objects(Bucket=bucket_name, Delete=delete_keys)
                print("Standard objects deleted")
            except ClientError as e:
                print(f"Error deleting standard objects: {e}")
            
            # Try to delete the bucket
            s3_client.delete_bucket(Bucket=bucket_name)
            print(f"Bucket {bucket_name} has been deleted successfully")
            return True
            
        except ClientError as e:
            print(f"Failed to delete bucket: {e}")
            print("Possible reasons for failure:")
            print("1. Insufficient permissions - check your IAM role/user permissions")
            print("2. Bucket policy restrictions - check the bucket policy")
            print("3. Bucket might be in a locked state - check if it has object lock enabled")
            print("4. Bucket might not be empty - there might be objects that couldn't be listed/deleted")
            return False

# Example usage
if __name__ == "__main__":
    bucket_name = "de-week16-gp-bucket"
    delete_bucket(bucket_name)

# import boto3

# def delete_bucket(bucket_name):
#     """
#     Delete an S3 bucket using boto3.
    
#     Args:
#         bucket_name (str): Name of the bucket to delete
#     """
#     # Create an S3 client
#     s3_client = boto3.client('s3')
    
#     # First, you need to empty the bucket as you can't delete a bucket that contains objects
#     # List all object versions (if versioning is enabled)
#     paginator = s3_client.get_paginator('list_object_versions')
    
#     for page in paginator.paginate(Bucket=bucket_name):
#         # Delete objects
#         if 'Versions' in page:
#             for version in page['Versions']:
#                 s3_client.delete_object(
#                     Bucket=bucket_name,
#                     Key=version['Key'],
#                     VersionId=version['VersionId']
#                 )
                
#         # Delete delete markers
#         if 'DeleteMarkers' in page:
#             for delete_marker in page['DeleteMarkers']:
#                 s3_client.delete_object(
#                     Bucket=bucket_name,
#                     Key=delete_marker['Key'],
#                     VersionId=delete_marker['VersionId']
#                 )
    
#     # List and delete objects (for non-versioned buckets)
#     paginator = s3_client.get_paginator('list_objects_v2')
#     for page in paginator.paginate(Bucket=bucket_name):
#         if 'Contents' in page:
#             delete_keys = {'Objects': [{'Key': obj['Key']} for obj in page['Contents']]}
#             s3_client.delete_objects(Bucket=bucket_name, Delete=delete_keys)
    
#     # Now delete the empty bucket
#     s3_client.delete_bucket(Bucket=bucket_name)
#     print(f"Bucket {bucket_name} has been deleted successfully")

# # Example usage
# if __name__ == "__main__":
#     bucket_name = "de-week16-gp-bucket"
#     delete_bucket(bucket_name)