from flask import render_template


def upload_file_page():
    return render_template('upload_file.html')


def show_all_files_page():
    return "list of all files"


