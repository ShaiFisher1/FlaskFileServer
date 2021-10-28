import os

from flask import jsonify

UPLOADS_FOLDER = "C:\\Users\\adifi\\Desktop\\uploads_folder"

def get_files_list():
    files_dict = {}
    if len(os.listdir(UPLOADS_FOLDER)) != 0:
        for folder in os.listdir(UPLOADS_FOLDER):
            num = str(folder)
            file_path = os.path.join(UPLOADS_FOLDER, num)
            file_name = str(os.listdir(file_path)[0])
            files_dict[num] = file_name
        return jsonify(files_dict)
    else:
        return "There are no files"
