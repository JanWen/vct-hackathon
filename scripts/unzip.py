import os
import gzip, shutil


# Example usage
zip_file_path = "C:\\Users\\Jan\\Downloads\\esports-data"
output_folder = 'esport-data'

for root, dirs, files in os.walk(zip_file_path):
    for file in files:
        with gzip.open(os.path.join(root, file), 'rb') as f_in:
            file_name = os.path.basename(file).replace('.gz', '')
            output_path = os.path.join(output_folder, file_name)
            with open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)