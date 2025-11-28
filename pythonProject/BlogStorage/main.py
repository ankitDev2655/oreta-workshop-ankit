import os
import mimetypes
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from azure.storage.blob import (
    BlobServiceClient,
    ContentSettings,
    generate_blob_sas,
    BlobSasPermissions
)

# ------------------------------
#  LOAD ENVIRONMENT VARIABLES
# ------------------------------
load_dotenv()

storage_connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
account_name = os.getenv("AZURE_ACCOUNT_NAME")
account_key = os.getenv("AZURE_ACCOUNT_KEY")
container_name = os.getenv("AZURE_CONTAINER_NAME")

# ------------------------------
#  CONNECT TO STORAGE
# ------------------------------
blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)

# Create container safely
try:
    blob_service_client.create_container(container_name)
    print("Container created!")
except Exception:
    print("Container already exists.")

# ------------------------------
#  UPLOAD + SAS
# ------------------------------
def upload_and_get_sas(local_path):

    if not os.path.exists(local_path):
        print("❌ File not found:", local_path)
        return

    file_name = os.path.basename(local_path)
    # blob_path = f"november/{file_name}"
    blob_path = file_name
    

    mime_type, _ = mimetypes.guess_type(file_name)
    if mime_type is None:
        mime_type = "application/octet-stream"

    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=blob_path
    )

    with open(local_path, "rb") as file:
        blob_client.upload_blob(
            file,
            overwrite=True,
            content_settings=ContentSettings(content_type=mime_type)
        )

    print(f"Uploaded → {file_name}")

    expiry_time = datetime.now(timezone.utc) + timedelta(hours=1)

    sas_token = generate_blob_sas(
        account_name=account_name,
        account_key=account_key,
        container_name=container_name,
        blob_name=blob_path,
        permission=BlobSasPermissions(read=True),
        expiry=expiry_time
    )

    sas_url = f"https://{account_name}.blob.core.windows.net/{container_name}/{blob_path}?{sas_token}"

    print("\n🔗 SAS URL:")
    print(sas_url)

    return sas_url


# ------------------------------
#  RUN
# ------------------------------
upload_and_get_sas("./files/first.jpg")