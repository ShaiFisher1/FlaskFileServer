# from flask import render_template
#
# def upload_file_page():
#     return render_template('upload_file.html')
#
#
# def show_all_files_page():
#     return render_template('get_file.html')
#
#
# def update_file_page():
#     return render_template('update_file.html')
#
#
# def get_file_by_num_page():
#     return render_template('get_file.html')

from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("main.html")

@views.route("/get_file")
def get_file():
    print("in get file html")
    return render_template("get_file.html")

@views.route("/update_file")
def update_file():
    print("in update file html")
    return render_template("update_file.html")
