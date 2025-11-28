import os
from dotenv import load_dotenv

from azure.storage.blob import BlobServiceClient
from azure.storage.blob import ContentSettings
import mimetypes

# ------------------------------
#  LOAD ENVIRONMENT VARIABLES
# ------------------------------
load_dotenv()



storage_connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = os.getenv("AZURE_CONTAINER_NAME")


blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)




try:
    container_client = blob_service_client.create_container(container_name)
    print("Container created!")
except Exception as e:
    print("Error creating container:", e)


# Current Container List 
print("\nCurrent containers:")
for c in blob_service_client.list_containers():
    print(" -", c['name'])
    

# Uploading Multiple files 
file_folder = './files'
for file_name in os.listdir(file_folder):
    blob_obj = blob_service_client.get_blob_client(
        container=container_name,
        blob=f"november/{file_name}"
    )
    print(f'Uploading file: {file_name}...')
    
    mime_type, _ = mimetypes.guess_type(file_name)
    
    
    with open(os.path.join(file_folder, file_name), mode='rb') as file_data:
        blob_obj.upload_blob(
            file_data,
            overwrite=True,
            content_settings=ContentSettings(content_type=mime_type)
        )

