import io
from io import BytesIO
from google.cloud import storage
import os
import json

credential_path = "utils\secrets.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

storage_client = storage.Client.from_service_account_json(credential_path)
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

def delete_blob(bucket_name, blob_name):
    blob = bucket.blob(blob_name)
    blob.delete()
    print(f"Blob {blob_name} deleted.")

def list_blobs_with_prefix(prefix:str, delimiter=None):
    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket, prefix=prefix, delimiter=delimiter)
    # Note: The call returns a response only when the iterator is consumed.
    names =  [blob.name for  blob in blobs]
    return names[1:]

def download_blob_into_memory(blob_name):
    blob = bucket.blob(blob_name)
    contents = blob.download_as_string()
    return contents

# print(list_blobs_with_prefix('results'))
# print(json.loads(download_blob_into_memory('results/video_talking_dog.json')))

audio_dummy = {"0_10": {"prediction": "positive", "sentence": "I am writing the first sentence", "start": 0, "stop": 10}, 
"10_20": {"prediction": "negative", "sentence": "I am writing the second sentence", "start": 10, "stop": 20}, 
"20_30": {"prediction": "negative", "sentence": "I am writing the third sentence", "start": 20, "stop": 30}, 
"30_40": {"prediction": "neutral", "sentence": "I am writing the fourth sentence", "start": 30, "stop": 40}, 
"40_50": {"prediction": "neutral", "sentence": "I am writing the fifth sentence", "start": 40, "stop": 50}, 
"50_60": {"prediction": "positive", "sentence": "I am writing the sixth sentence", "start": 50, "stop": 60},
"60_70": {"prediction": "neutral", "sentence": "I am writing the seventh sentence", "start": 60, "stop": 70}, 
"70_80": {"prediction": "positive", "sentence": "I am writing the eighth sentence", "start": 70, "stop": 80}, 
"80_90": {"prediction": "neutral", "sentence": "I am writing the nigth sentence", "start": 80, "stop": 90}}

video_dummy = {'0_10': {'positive': 1, 'neutral': 2, 'negative': 3}, 
'10_20': {'positive': 1, 'neutral': 2, 'negative': 3}, 
'20_30': {'positive': 1, 'neutral': 2, 'negative': 3}, 
'30_40': {'positive': 1, 'neutral': 2, 'negative': 3}, 
'40_50': {'positive': 1, 'neutral': 2, 'negative': 3}, 
'50_60': {'positive': 1, 'neutral': 2, 'negative': 3}, 
"60_70": {'positive': 1, 'neutral': 2, 'negative':3},
'70_80': {'positive': 1, 'neutral': 2, 'negative': 3}, 
'80_90': {'positive': 1, 'neutral': 2, 'negative': 3}}


# print(upload_blob_from_memory('edaa_bucket', json.dumps(audio_dummy),'results/audio_talking_dog.json'))