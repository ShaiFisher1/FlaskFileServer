import os

from flask import Flask, request, jsonify, make_response, send_from_directory

UPLOADS_FOLDER = "C:\\Users\\adifi\\Desktop\\uploads_folder"
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# uploads a file and gets its id back
@app.route('/files', methods=['POST'])
def upload_file():
    next_id = get_largest_id_number() + 1
    save_path = os.path.join(UPLOADS_FOLDER, str(next_id))
    file = request.files['file']
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file.save(os.path.join(save_path, file.filename))
    return f"The file uploaded, The id of the file is {next_id}"


# gets all the files in a list
@app.route('/files', methods=['GET'])
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


@app.route('/files/lala/<name>')
def update_file(name):
    try:
        file_path = os.path.join(UPLOADS_FOLDER,
                                 str(name))  # adds the id given to the path
        file_name = os.listdir(file_path)[
            0]  # there is only one file in each dir
        os.remove(os.path.join(file_path, file_name))

    except FileNotFoundError:
        return f'file with the id number: {name} not found and therefore cannot be updated', 404


# gets a number and returns the file
@app.route('/files/<name>')
def get_file(name):
    try:
        file_path = os.path.join(UPLOADS_FOLDER,
                                 str(name))  # adds the id given to the path
        file_name = os.listdir(file_path)[
            0]  # there is only one file in each dir
        return send_from_directory(file_path, file_name,
                                   as_attachment=True)
    except FileNotFoundError:
        return f'file with the id number: {name} not found', 404


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
    app.run()
