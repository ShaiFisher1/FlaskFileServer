import os

from flask import Flask, request, jsonify, make_response, send_from_directory, \
    render_template

UPLOADS_FOLDER = "C:\\Users\\adifi\\Desktop\\uploads_folder"
app = Flask(__name__)
from views import upload_file_page, show_all_files_page, update_file_page, \
    get_file_by_num_page

# ------------------ only views (all html pages) ----------
# todo understand the purpose of the second parameter.
app.add_url_rule('/show_all_files', '', show_all_files_page, methods=['GET'])


# app.add_url_rule('/upload_file', '', upload_file_page, methods=['GET'])
# app.add_url_rule('/update_file', '', update_file_page(), methods=['GET'])
# app.add_url_rule('/get_file', '', get_file_by_num_page(), methods=['GET'])

# ----------------- end views only --------------


# todo add_url_rule for views (which are just pages)
#  make sure all rest api requests are /api/v1

# app.register_blueprint(second, url_prefix="")

@app.route('/api/v1/files', methods=['GET'])
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


@app.route("/")
def home():
    return render_template("home.html")


# uploads a file and gets its id back
@app.route('/api/v1/files', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        next_id = get_largest_id_number() + 1
        save_path = os.path.join(UPLOADS_FOLDER, str(next_id))
        file = request.files['file']
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        file.save(os.path.join(save_path, file.filename))
    return f"The file uploaded, The id of the file is {next_id}"


@app.route('/api/v1/files/<file_id>', methods=['PUT'])
def update_file(file_id):
    try:
        file_path = os.path.join(UPLOADS_FOLDER,
                                 str(file_id))  # adds the id given to the path
        file_name = os.listdir(file_path)[
            0]  # there is only one file in each dir
        os.remove(os.path.join(file_path, file_name))
        file = request.files['file']
        file.save(os.path.join(file_path, file.filename))

    except FileNotFoundError:
        return f'file with the id number: {file_id} not found and therefore cannot be updated', 404


# todo why v2?
@app.route('/api/v2/files/<file_id>', methods=['GET'])
def get_file(file_id):
    try:
        file_path = os.path.join(UPLOADS_FOLDER,
                                 str(file_id))  # adds the id given to the path
        file_name = os.listdir(file_path)[
            0]  # there is only one file in each dir
        return send_from_directory(file_path, file_name,
                                   as_attachment=True)
    except FileNotFoundError:
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


if __name__ == '__main__':
    app.run(debug=True)
