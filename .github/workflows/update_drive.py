import os
import pathlib
from gdrive_auth import Create_Service
from gdrive_utility import (
    get_existing_files_recursive,
    upload_file_or_folder,
    delete_items_not_in_local
)

OAUTH2_SECRET = 'credentials.json'
SCOPES = ['https://www.googleapis.com/auth/drive']
API_TYPE = 'drive'
API_VERSION = 'v3'

LOCAL_FOLDER = 'shared'
GDRIVE_FOLDER_ID = 'YOUR_FOLDER_ID'

def main():
    if not os.path.isdir(LOCAL_FOLDER):
        print(f"Folder '{LOCAL_FOLDER}' not found.")
        return

    drive_service = Create_Service(OAUTH2_SECRET, API_TYPE, API_VERSION, SCOPES)

    print("📝 Getting file list from google drive...")
    existing_files = get_existing_files_recursive(GDRIVE_FOLDER_ID, drive_service)

    print("⬆️ Uploading local files/folders to Google Drive...")
    upload_file_or_folder(
        local_base_path=LOCAL_FOLDER,
        parent_drive_folder_id=GDRIVE_FOLDER_ID,
        drive_service=drive_service,
        existing_items=existing_files
    )

    print("🧹 Removing non-existent local files/directories from Google Drive...")
    delete_items_not_in_local(
        local_base_path=LOCAL_FOLDER,
        parent_drive_folder_id=GDRIVE_FOLDER_ID,
        drive_service=drive_service,
        existing_items=existing_files
    )

if __name__ == '__main__':
    main()
