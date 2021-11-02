
# TODO imports look unrelevant
import os
import re

# import of the functions from the manager file, and the global variable ERROR
from manager import ERROR, get_files_list_manager, upload_file_manager, \
    update_file_manager, get_file_by_id_manager

# TODO some imports look unrelevant
from flask import Flask, request, jsonify, make_response, send_from_directory, \
    render_template

# import of the Blueprint TODO maybe remove because i dont know to explain about blueprint
from views import views

app = Flask(__name__)

app.register_blueprint(views, url_prefix="/")

@app.route('/api/v1/files', methods=['GET'])

def get_files_handler():
    """The funciton returns a list of all the files"""

    result = get_files_list_manager()
    return result


@app.route('/api/v1/files', methods=['POST'])
def upload_file_handler():
    """The funciton gets a file and uploads the file, the id allocated to the file is returned"""

    file = request.files['file']
    result = upload_file_manager(file)
    return result


@app.route('/api/v1/files/<file_id>', methods=['PUT'])
def update_file(file_id):
    """The funciton gets a file and an id and updates the id with the updated file. if the id given is not found, an error is returned"""

    file = request.files['file']
    result = update_file_manager(file_id, file)
    if result!=ERROR:
        return result
    else:
        return str(ERROR)


@app.route('/api/v1/files/<file_id>', methods=['GET'])
def get_file_by_id(file_id):
    """The funciton gets an id and returns the file that matches the given id"""

    result = get_file_by_id_manager(file_id)
    return result


if __name__ == '__main__':
    app.run(debug=True)
