from flask import Blueprint, render_template

ww = Blueprint("ww", __name__, template_folder="templates", static_folder="static")


@ww.route("/")
def index():
    return render_template('index.html')