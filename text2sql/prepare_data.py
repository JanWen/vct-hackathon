import boto3
import gzip
import os
from config import *

local_directory = './esports_data/tmp'


s3_source = boto3.client('s3', region_name='us-west-2')
source_bucket = "https://vcthackathon-data.s3.us-west-2.amazonaws.com"
source_bucket_name = 'vcthackathon-data'
source_s3_directory = 'vct-challengers/esports-data/'

s3_dest = s3
dest_bucket_name = bucket_name
dest_s3_directory = 'data/vct-challengers/'

# List objects in the specified directory
response = s3_source.list_objects_v2(Bucket=source_bucket_name, Prefix=source_s3_directory)

files_to_dl = [obj['Key'] for obj in response['Contents'] if obj['Key'].endswith('.json.gz')]


def flatten_file(file_name):
    data = []
    old_path = file_name
    new_path = file_name+".flat"
    with open(old_path, encoding="utf8") as f:
        data = json.load(f)

    with open(new_path, "w", encoding="utf8") as f2:
        for entry in data:
            f2.write(json.dumps(entry) + "\n")
    
    os.remove(old_path)
    os.rename(new_path, old_path)


def unzip_file(source, dest):
    with gzip.open(source, 'rb') as f_in:
        with open(dest, 'wb') as f_out:
            f_out.write(f_in.read())

def move_files():
    if not os.path.exists(local_directory):
        os.makedirs(local_directory)
    for s3_key in files_to_dl:
        file_name = os.path.basename(s3_key)
        local_gz_path = os.path.join(local_directory, file_name)
        local_json_path = local_gz_path[:-3]  # Remove the .gz extension for the output file
        
        # remove json extesion
        s3_source.download_file(source_bucket_name, s3_key, local_gz_path)
        unzip_file(local_gz_path, local_json_path)
        os.remove(local_gz_path)
        flatten_file(local_json_path)

        json_file_name = os.path.basename(local_json_path)
        folder_name = json_file_name[:-5]
        upload_path = dest_s3_directory + folder_name + "/" + json_file_name
        print("Uploading to", upload_path)
        s3_dest.upload_file(local_json_path, dest_bucket_name, upload_path)
        os.remove(local_json_path)


    os.removedirs(local_directory)