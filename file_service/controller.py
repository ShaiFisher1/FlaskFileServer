import os
import re

from manager import ERROR, get_files_list_manager, upload_file_manager, \
    update_file_manager, get_file_by_id_manager

from flask import Flask, request, jsonify, make_response, send_from_directory, \
    render_template
# import of the Blueprint
from views import views
# a global variable of the location where the files are saved on
app = Flask(__name__)

app.register_blueprint(views, url_prefix="/")

@app.route('/api/v1/files', methods=['GET'])
def get_files_handler():
    result = get_files_list_manager()
    return result


# client uploads a file and gets it's id back
@app.route('/api/v1/files', methods=['POST'])
def upload_file_handler():
    file = request.files['file']
    result = upload_file_manager(file)
    return result

#todo why is file sent as an request and the  id not?
@app.route('/api/v1/files/<file_id>', methods=['PUT'])
def update_file(file_id):
    file = request.files['file']
    result = update_file_manager(file_id, file)
    if result!=ERROR:
        return result
    else:
        return str(ERROR)

@app.route('/api/v1/files/<file_id>', methods=['GET'])
def get_file_by_id(file_id):
    result = get_file_by_id_manager(file_id)
    return result


if __name__ == '__main__':
    app.run(debug=True)
