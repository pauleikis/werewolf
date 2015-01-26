from flask import Blueprint, render_template

ww = Blueprint(
    "ww",
    __name__,
    template_folder="templates",
    static_folder="static"
)


ROLES = list(map(str.strip,
                 open("ww/data/roles", encoding="utf-8").readlines()))

PLAYERS = list(map(str.strip,
                   open("ww/data/players", encoding="utf-8").readlines()))


@ww.route("/")
def index():
    return render_template('graphs.html')


@ww.route("/new")
def new():
    return render_template('new_game.html', roles=ROLES, players=PLAYERS)
