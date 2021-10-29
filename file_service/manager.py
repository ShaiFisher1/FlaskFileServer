import os
import sys

from flask import jsonify, send_from_directory

UPLOADS_FOLDER = "C:\\Users\\adifi\\Desktop\\uploads_folder"

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
        return "There are no files"

def upload_file_manager(file):
    next_id = get_largest_id_number() + 1
    save_path = os.path.join(UPLOADS_FOLDER, str(next_id))
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file.save(os.path.join(save_path, file.filename))
    return f"The file uploaded, The id of the file is {next_id}"


def update_file_manager(file_id, file):
    if(is_id_valid(file_id)):
        file_path = os.path.join(UPLOADS_FOLDER,
                                 str(file_id))  # adds the id given to the path
        file_name = os.listdir(file_path)[
            0]  # there is only one file in each dir
        os.remove(os.path.join(file_path, file_name))
        file.save(os.path.join(file_path, file.filename))
    # except FileNotFoundError:
        return "file updated"
    else:
        return f'file with the id number: {file_id} not found and therefore cannot be updated', 404

def get_file_by_id_manager(file_id):
    if (is_id_valid(file_id)):
        file_path = os.path.join(UPLOADS_FOLDER,
                                 str(file_id))  # adds the id given to the path
        file_name = os.listdir(file_path)[
            0]  # there is only one file in each dir
        return send_from_directory(file_path, file_name,as_attachment=True)
    else:
        return f'file with the id number: {file_id} not found', 404


def get_largest_id_number(folder=UPLOADS_FOLDER):
    """
    todo change the documentation to what the function does
    returns the number that is to be assigned to the next file
    that will be uploaded
    :param folder:
    :return:
    """
    return max([int(x) for x in os.listdir(folder)], default=0)



def is_id_valid(id):
    # checks if given id is valid
    return True
