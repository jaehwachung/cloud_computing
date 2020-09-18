import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

try:
    print("한국방송통신대학교 4학년 2학기 클라우드 컴퓨팅")

    connect_str = "<연결 문자열>"
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_name = "mall-blob-container"
    
    up_file_name = "quickstart_hello.txt"
    local_file_name = "quickstart-hello-download.txt"
    
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=up_file_name)

    print("\nDownloading blob to \n\t" + up_file_name)

    with open(local_file_name, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())

except Exception as ex:
    print('Exception:')
    print(ex)