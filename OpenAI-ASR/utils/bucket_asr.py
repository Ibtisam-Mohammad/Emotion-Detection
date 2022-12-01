import io
from io import BytesIO
from google.cloud import storage
import os
credential_path = "secrets/mercurial-snow.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

storage_client = storage.Client.from_service_account_json("secrets/mercurial-snow.json")
bucket = storage.Bucket(storage_client, 'edaa_bucket')

def list_blobs(folder='chunks/'):
    blobs = bucket.list_blobs(prefix=folder)
    for blob in blobs:
        if not blob.name.endswith('/'):
            print(blob.name)


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

def upload_blob_from_memory(bucket_name, contents, destination_blob_name):
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string(contents)

def download_blob(bucket_name, source_blob_name, destination_file_name):
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print("Downloaded storage object {} from bucket {} to local file {}.".format(
            source_blob_name, bucket_name, destination_file_name))
            
def download_blob_into_memory(blob_name):
    blob = bucket.blob(blob_name)
    contents = blob.download_as_string()
    return contents

def delete_blob(bucket_name, blob_name):
    blob = bucket.blob(blob_name)
    blob.delete()
    print(f"Blob {blob_name} deleted.")

# list_blobs()
# upload_blob('edaa_bucket','D:/Yolov7/YOLO/subprocess_file.py','subprocess.txt')
# download_blob('edaa_bucket', 'subprocess.txt', 'delete.py')
# delete_blob('edaa_bucket', 'subprocess.txt')