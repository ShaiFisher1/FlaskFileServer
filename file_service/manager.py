import os
import re
import sys

from flask import jsonify, send_from_directory

UPLOADS_FOLDER = "C:\\Users\\adifi\\Desktop\\uploads_folder"
ERROR = -1

def get_files_list_manager():
    files_dict = {}
    if len(os.listdir(UPLOADS_FOLDER)) != 0:
        for folder in os.listdir(UPLOADS_FOLDER):
            num = str(folder)
            file_path = os.path.join(UPLOADS_FOLDER, num)
            file_name = str(os.listdir(file_path)[0])
            files_dict[num] = file_name
        return jsonify(files_dict)
    else:
        return f"There are no files", 500

def upload_file_manager(file):
    next_id = get_largest_id_number() + 1
    save_path = os.path.join(UPLOADS_FOLDER, str(next_id))
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file.save(os.path.join(save_path, file.filename))
    return f"The file uploaded, The id of the file is {next_id}"

def update_file_manager(file_id, file):
    try:
        file_path = os.path.join(UPLOADS_FOLDER, str(file_id))  # adds the id given to the path
        file_name = os.listdir(file_path)[0]  # there is only one file in each dir
        os.remove(os.path.join(file_path, file_name))
        file.save(os.path.join(file_path, file.filename))
        return file_id
    except:
        return ERROR    

def get_file_by_id_manager(file_id):
    file_path = os.path.join(UPLOADS_FOLDER, str(file_id))  # adds the id given to the path
    file_name = os.listdir(file_path)[0]  # there is only one file in each dir
    return send_from_directory(file_path, file_name,as_attachment=True)

def get_largest_id_number(folder=UPLOADS_FOLDER):
    return max(
        [int(x) for x in os.listdir(folder)]
        , default=0)


