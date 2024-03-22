import boto3

def copy_files_between_buckets(source_bucket_name, destination_bucket_name):
    # Initialize S3 client
    s3 = boto3.client('s3')

    # List all objects in the source bucket
    response = s3.list_objects_v2(Bucket=source_bucket_name)

    # Iterate through each object
    for obj in response.get('Contents', []):
        # Get the object key
        source_key = obj['Key']
        # Extract the filename
        filename = source_key.split('/')[-1]
        # Generate the destination key
        destination_key = f'test_folder/{filename}'
        # Copy the object to the destination bucket
        s3.copy_object(
            CopySource={'Bucket': source_bucket_name, 'Key': source_key},
            Bucket=destination_bucket_name,
            Key=destination_key
        )

if __name__ == "__main__":
    # Specify your source and destination bucket names
    source_bucket_name = 'myy-demo-s3'
    destination_bucket_name = 'aws-ap-south'

    # Call the function to copy files between buckets
    copy_files_between_buckets(source_bucket_name, destination_bucket_name)
