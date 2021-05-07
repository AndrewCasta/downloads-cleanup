import os
import shutil
from util.files_folders import (
    delete_files,
    delete_file_types,
    completed_folder,
    delete_folder,
)

# list of files or extentions
# check all files in folder against type & move to delete
for dirpath, dirnames, files in os.walk(completed_folder):
    for file in files:
        if file in delete_files or [ext in file for ext in delete_file_types][0]:
            file_path = f"{dirpath}\{file}"
            delete_folder_path = f"{delete_folder}\{file}"
            shutil.move(file_path, delete_folder_path)

    # check for empty folders & delete
for dirpath, dirnames, files in os.walk(completed_folder):
    if not dirnames and not files and dirpath not in delete_folder:
        try:
            shutil.move(dirpath, delete_folder)
        except shutil.Error:
            os.rmdir(dirpath)