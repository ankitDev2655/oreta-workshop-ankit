import os
from dotenv import load_dotenv
from azure.storage.blob import generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta

# ------------------------------
#  LOAD ENVIRONMENT VARIABLES
# ------------------------------
load_dotenv()

blob_name = "november/first.jpg"

account_name = os.getenv("AZURE_ACCOUNT_NAME")
account_key = os.getenv("AZURE_ACCOUNT_KEY")
container_name = os.getenv("AZURE_CONTAINER_NAME")

sas_token = generate_blob_sas(
    account_name=account_name,
    container_name=container_name,
    blob_name=blob_name,
    account_key=account_key,
    permission=BlobSasPermissions(read=True),
    expiry=datetime.utcnow() + timedelta(hours=1)
)

url = f"https://{account_name}.blob.core.windows.net/{container_name}/{blob_name}?{sas_token}"
print(url)
