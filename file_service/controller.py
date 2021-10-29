import os

# from manager import get_files_list_manager, upload_file_manager, \
#     update_file_manager, get_file_by_id_manager

from .manager import get_files_list_manager, upload_file_manager, \
    update_file_manager, get_file_by_id_manager

from flask import Flask, request, jsonify, make_response, send_from_directory, \
    render_template

UPLOADS_FOLDER = "C:\\Users\\adifi\\Desktop\\uploads_folder"
app = Flask(__name__)


# from views import upload_file_page, show_all_files_page, update_file_page
# from views import get_file_by_num_page


# ------------------ only views (all html pages) ----------
# todo understand the purpose of the second parameter.
# app.add_url_rule('/get_file', '', get_file_by_num_page, methods=['GET'])
# app.add_url_rule('/upload_file', '', upload_file_page, methods=['GET'])
# app.add_url_rule('/update_file', '', update_file_page, methods=['GET'])

# ----------------- end views only --------------

# todo add_url_rule for views (which are just pages)
#  make sure all rest api requests are /api/v1

# app.register_blueprint(second, url_prefix="")

# @app.route("/")
# def home():
#     return render_template("main.html")

@app.route('/api/v1/files', methods=['GET'])
def get_files_handler():
    result = get_files_list_manager()
    return result


# uploads a file and gets its id back
@app.route('/api/v1/files', methods=['POST'])
def upload_file_handler():
    file = request.files['file']
    result = upload_file_manager(file)
    return result


@app.route('/api/v1/files/<file_id>', methods=['PUT'])
def update_file(file_id):
    file = request.files['file']
    result = update_file_manager(file_id, file)
    return result


# todo why v2?
@app.route('/api/v2/files/<file_id>', methods=['GET'])
def get_file_by_id(file_id):
    print("in get file by id")
    result = get_file_by_id_manager(file_id)
    return result


if __name__ == '__main__':
    app.run(debug=True)
