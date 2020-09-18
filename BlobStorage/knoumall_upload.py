import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

try:
  print("한국방송통신대학교 4학년 2학기 클라우드 컴퓨팅")
  connect_str = "<연결 문자열>"
  blob_service_client = BlobServiceClient.from_connection_ string(connect_str)
  container_name = "cloud-shop-cc"

  local_file_name = "quickstart" + str(uuid.uuid4()) + ".txt" 
  upload_file_path = local_file_name
  
  file = open(upload_file_path,'w') 
  file.write("Hello, World!") 
  file.close( )

  blob_client = blob_service_client.get_blob_client(container=container_ name, blob=local_file_name)
  
  print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

  # Upload the created file
  with open(upload_file_path, "rb") as data:
    blob_client.upload_blob(data)

except Exception as ex: 
  print('Exception:') 
  print(ex)
