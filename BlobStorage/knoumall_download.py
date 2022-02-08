import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

try:
  print("한국방송통신대학교 4학년 2학기 클라우드 컴퓨팅")

  connect_str = "<연결 문자열>"
  blob_service_client = BlobServiceClient.from_connection_string(connect_str)
  container_name = "<컨테이너 이름>"
  
  # ex) local_file_name = 'quickstartc690f445-bf9f-4b4f-8700-d4ad3ca3a663.txt'
  local_file_name = "<다운받을 파일 이름>" 
  # ex) local_path = '.'
  local_path = '<다운받을 위치>'
  
  blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
  
  # Download the blob to a local file
  # Add 'DOWNLOAD' before the .txt extension so you can see both files in the data directory
  download_file_path = os.path.join(local_path, str.replace(local_file_name ,'.txt', 'DOWNLOAD.txt'))
  print("\nDownloading blob to \n\t" + download_file_path)

  with open(download_file_path, "wb") as download_file:
    download_file.write(blob_client.download_blob().readall())

except Exception as ex: 
  print('Exception:')
  print(ex)
  
