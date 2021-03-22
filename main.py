from azure.storage.blob import BlockBlobService, PublicAccess
import os, shutil, sys
from datetime import date
from dotenv import load_dotenv

load_dotenv()
today = date.today()

def upload_files():

    try:
        current_date = today.strftime("%m-%d-%Y")

        account_name = os.getenv('ACCOUNT_NAME')
        account_key = os.getenv('ACCOUNT_KEY')

        # Create the BlockBlockService that is used to call the Blob service for the storage account
        block_blob_service = BlockBlobService(account_name=account_name, account_key=account_key)


        container_name = input("Enter the container name: ")
        block_blob_service.create_container(container_name)

        # Set the permission so the blobs are public.
        block_blob_service.set_container_acl(container_name, public_access=PublicAccess.Container)

        full_path_to_folder = input("Enter the path to the folder to be uploaded: ")
        destination_file_name = input("Enter the destination file name: ")
        destination_file_path = current_date + '/' + destination_file_name
        zipped_folder = shutil.make_archive(destination_file_name, 'zip', full_path_to_folder)
        
        print("Zipped folder = " + full_path_to_folder)
        print("\nUploading to Blob storage as blob" + destination_file_path)

        # Upload the created file, use local_file_name for the blob name
        block_blob_service.create_blob_from_path(container_name, destination_file_path, zipped_folder)

        # List the blobs in the container
        print('\n----------------------------------\n')
        print("List blobs in the container")
        generator = block_blob_service.list_blobs(container_name)
        for blob in generator:
            print("\t Blob name: " + blob.name)
        print('\n----------------------------------\n')

        delete_response = input(f'inished uploading.Do you want to delete local zipped file "{destination_file_name}" (Y/N) ?:' )
        if delete_response == 'Y':
            os.remove(destination_file_name + '.zip')

        # Clean up resources. This includes the container and the temp files
        # block_blob_service.delete_container(container_name)

    except Exception as e:
        print(e)

# Main method.
if __name__ == '__main__':
    upload_files()
