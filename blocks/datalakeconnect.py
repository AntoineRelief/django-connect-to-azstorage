import os, uuid, sys
from azure.storage.filedatalake import DataLakeServiceClient
from azure.core._match_conditions import MatchConditions
from azure.storage.filedatalake._models import ContentSettings
from django.conf import settings

def initialize_storage_account(storage_account_name, storage_account_key):
  try:  
    global service_client

    service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
      "https", storage_account_name), credential=storage_account_key)
    
  except Exception as e:
    print(e)

def create_file_system():
  try:
    global file_system_client

    file_system_client = service_client.create_file_system(file_system="my-file-system")
    
  except Exception as e:
    print(e)

def create_directory():
  try:
    file_system_client.create_directory("my-directory")
    
  except Exception as e:
    print(e)

def rename_directory():
  try: 
    file_system_client = service_client.get_file_system_client(file_system="my-file-system")
    directory_client = file_system_client.get_directory_client("my-directory")
       
    new_dir_name = "my-directory-renamed"
    directory_client.rename_directory(new_name=directory_client.file_system_name + '/' + new_dir_name)

  except Exception as e:
    print(e)

def delete_directory():
  try:
    file_system_client = service_client.get_file_system_client(file_system="my-file-system")
    directory_client = file_system_client.get_directory_client("my-directory")

    directory_client.delete_directory()
  except Exception as e:
    print(e)

def upload_file_to_directory():
  try:
    file_system_client = service_client.get_file_system_client(file_system="my-file-system")

    directory_client = file_system_client.get_directory_client("my-directory")
        
    file_client = directory_client.create_file("uploaded-file.txt")
    local_file = open("C:\\file-to-upload.txt",'r')

    file_contents = local_file.read()

    file_client.append_data(data=file_contents, offset=0, length=len(file_contents))

    file_client.flush_data(len(file_contents))

  except Exception as e:
    print(e)

def upload_file_to_directory_bulk():
  try:
    file_system_client = service_client.get_file_system_client(file_system="my-file-system")

    directory_client = file_system_client.get_directory_client("my-directory")
    
    file_client = directory_client.get_file_client("uploaded-file.txt")

    local_file = open("C:\\file-to-upload.txt",'r')

    file_contents = local_file.read()

    file_client.upload_data(file_contents, overwrite=True)

  except Exception as e:
    print(e)

def download_file_from_directory():
  try:
    file_system_client = service_client.get_file_system_client(file_system="my-file-system")

    directory_client = file_system_client.get_directory_client("my-directory")
    
    local_file = open("C:\\file-to-download.txt",'wb')

    file_client = directory_client.get_file_client("uploaded-file.txt")

    download = file_client.download_file()

    downloaded_bytes = download.readall()

    local_file.write(downloaded_bytes)

    local_file.close()

  except Exception as e:
    print(e)

def list_directory_contents():
  try:
      
    file_system_client = service_client.get_file_system_client(file_system="my-file-system")

    paths = file_system_client.get_paths(path="my-directory")

    for path in paths:
      print(path.name + '\n')

  except Exception as e:
    print(e)

def retrieve_file(id):
  initialize_storage_account(settings.STORAGE_ACCOUNT_NAME, settings.STORAGE_ACCOUNT_KEY)
  file_system = service_client.get_file_client('block1', '{}.json'.format(id))
  file = file_system.download_file()
  content = file.readall()
  return content
