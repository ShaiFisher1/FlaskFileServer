import os
import re
import sys

from flask import jsonify, send_from_directory

# this folder is where the files uploaded by the client are saved in
UPLOADS_FOLDER = "C:\\Users\\adifi\\Desktop\\uploads_folder"

ERROR = -1

def get_files_list_manager():
    """The funciton returns a dictionary of all the files, if there are no files returns an error"""

    files_dict = {}
    if len(os.listdir(UPLOADS_FOLDER)) != 0: # checking that the folder is not empty
        for folder in os.listdir(UPLOADS_FOLDER):
            num = str(folder)
            file_path = os.path.join(UPLOADS_FOLDER, num)
            file_name = str(os.listdir(file_path)[0]) # accessing the 0 place because there is only one file per folder
            files_dict[num] = file_name # the key will be the id of the file and the value is the name of the file 
        return jsonify(files_dict) # TODO is jsonify needed?
    else:
        return f"There are no files"

def upload_file_manager(file):
    """The funciton gets a file and uploads the file.
       a new folder is allocated to the file (the id)"""

    next_id = get_largest_id_number() + 1
    save_path = os.path.join(UPLOADS_FOLDER, str(next_id)) # the path where the new file uploaded will be saved
    if not os.path.exists(save_path): #making sure the id allocated to the new file does not exist already
        os.makedirs(save_path)
    file.save(os.path.join(save_path, file.filename))
    return f"The file uploaded, The id of the file is {next_id}" 

def update_file_manager(file_id, file):
    """The funciton gets a file and an id and updates the id with the updated file.
     if suceeded, the id of the file is returned, else, an error is returned"""
    try:
        file_path = os.path.join(UPLOADS_FOLDER, str(file_id)) # adds the id given to the path to know where to update the file
        file_name = os.listdir(file_path)[0] # accessing the 0 place (because there is only one file per folder) to get the old file name
        os.remove(os.path.join(file_path, file_name)) 
        file.save(os.path.join(file_path, file.filename))
        return file_id
    except:
        return ERROR    

def get_file_by_id_manager(file_id):
    """The funciton gets an id and returns the file that matches the given id"""

    file_path = os.path.join(UPLOADS_FOLDER, str(file_id))  # searches for the path according to the id received 
    file_name = os.listdir(file_path)[0] # accessing the 0 place (because there is only one file per folder)
    return send_from_directory(file_path, file_name,as_attachment=True)

def get_largest_id_number(folder=UPLOADS_FOLDER): 
    """The funciton gets the largest id in the folder where the files are saved"""
    
    return max([int(x) for x in os.listdir(folder)], default=0)


