import os
from dotenv import load_dotenv

import mimetypes
from azure.storage.blob import BlobServiceClient, ContentSettings

# ------------------------------
#  LOAD ENVIRONMENT VARIABLES
# ------------------------------
load_dotenv()

storage_connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = os.getenv("AZURE_CONTAINER_NAME")


blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)


# Create container if not exists
try:
    blob_service_client.create_container(container_name)
    print("Container created!")
except Exception as e:
    print("Container already exists or error:", e)


# Upload file
def upload_file(local_path):
    if not os.path.exists(local_path):
        print("❌ File not found:", local_path)
        return
    
    file_name = os.path.basename(local_path)
    mime_type, _ = mimetypes.guess_type(file_name)
    if mime_type is None:
        mime_type = "application/octet-stream"

    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=f"november/{file_name}"
    )

    with open(local_path, "rb") as f:
        blob_client.upload_blob(
            f,
            overwrite=True,
            content_settings=ContentSettings(content_type=mime_type)
        )

    print(f"Uploaded → {file_name}")


# Call function
upload_file("./files/first.jpg")
