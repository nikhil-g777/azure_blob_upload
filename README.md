# Script to zip and upload the folder to azure blob storage

Steps : 
- Create a .env file with the following keys : 
    - ACCOUNT_NAME
    - ACCOUNT_KEY
- Install the required python dependenices by running the command "pip3 install -r requirements.txt"
- Run the the main script by running the command "python3 main.py" and follow the command line instructions

The script creates a zipped folder of the directory path mentioned and uploads it to a container in Azure as a blob