from db import db
from plots import win_ratio, points


def update():
    db.update()

    win_ratio.players()
    win_ratio.roles()
    points.players()
    points.roles()


if __name__ == "__main__":
    update()
