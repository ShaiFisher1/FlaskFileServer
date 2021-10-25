from flask import render_template


def upload_file_page():
    return render_template('upload_file.html')


def show_all_files_page():
    return render_template('show_all_files.html')


def update_file_page():
    return render_template('update_file.html')


def get_file_by_num_page():
    return render_template('get_file_by_num.html')
