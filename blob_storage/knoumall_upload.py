import os, io
from azure.storage.blob import BlobServiceClient

try:
  print("한국방송통신대학교 클라우드 컴퓨팅 Blob 파일 업로드)
  connect_str = "<연결 문자열>"
  blob_service_client = BlobServiceClient.from_connection_string(connect_str)
  container_name = "<컨테이너 이름>"

  local_file_name = "main_carousel.png" 

  blob_client = blob_service_client.get_blob_client(container="mall-blob-container", blob=local_file_name)
  input_stream = io.BytesIO(os.urandom(15))
  blob_client.upload_blob(input_stream, blob_type="BlockBlob")
        
  print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

except Exception as ex: 
  print('Exception:') 
  print(ex)
