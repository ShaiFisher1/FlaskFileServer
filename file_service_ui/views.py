
# here i create the Blueprint
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

@views.route("/upload_file")
def upload_file():
    print("in upload file html")
    return render_template("upload_file.html")

@views.route("/get_all_files")
def get_all_files():
    print("in get all files html")
    return render_template("get_all_files.html")


# Todo - i suggest you will do the last one as "delete file", like CRUD. if you will do it by yourself you will understand all the thinkg I did.
# If you want to keep the "Get all files" you can but tell me how you want it to look in the ui. 
