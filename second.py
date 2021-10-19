from flask import Blueprint, render_template

second = Blueprint("second", __name__, static_folder="static",
                   template_folder="templates")


@second.route("/files")
@second.route("/")
def files():
    return render_template("home.html")
