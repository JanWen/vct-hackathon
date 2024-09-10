import boto3
import gzip
import os

# Initialize S3 client
s3 = boto3.client('s3', region_name='us-west-2')

# Define the bucket and directory
bucket_name = 'vcthackathon-data'
s3_directory = 'vct-challengers/esports-data/'
local_directory = './esports_data_new/'

# Create local directory if it doesn't exist
if not os.path.exists(local_directory):
    os.makedirs(local_directory)

# List objects in the specified directory
response = s3.list_objects_v2(Bucket=bucket_name, Prefix=s3_directory)

# Download and decompress each .json.gz file
if 'Contents' in response:
    for obj in response['Contents']:
        s3_key = obj['Key']
        
        # Check if the object is a .json.gz file
        if s3_key.endswith('.json.gz'):
            file_name = os.path.basename(s3_key)
            local_gz_path = os.path.join(local_directory, file_name)
            local_json_path = local_gz_path[:-3]  # Remove the .gz extension for the output file

            # Download the .json.gz file
            s3.download_file(bucket_name, s3_key, local_gz_path)
            print(f'Downloaded: {file_name}')

            # Unpack the .gz file
            with gzip.open(local_gz_path, 'rb') as f_in:
                with open(local_json_path, 'wb') as f_out:
                    f_out.write(f_in.read())
            print(f'Unpacked: {local_json_path}')

            # Optionally, delete the .gz file after unpacking
            os.remove(local_gz_path)
            print(f'Removed: {local_gz_path}')
else:
    print('No files found in the specified directory.')
