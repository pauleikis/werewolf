import pandas as pd
import plotly.plotly as py
from plotly.graph_objs import Bar, Layout, Data, Figure
from db import db


def player_points():
    df = pd.DataFrame(
        [
            (player, calculate_points(player, game.players, game.winners))
            for game in db.load()
            for player in game.players
        ],
        columns=["Player", "Points"]
    ).groupby("Player").filter(lambda x: len(x) > 5).groupby("Player")

    df = df.sum() / df.count()

    return ((df - df.min()) / (df.max() - df.min()) * 100).astype("int").sort(
        "Points", ascending=0)


def player_points_plot():
    ps = player_points()
    points = Bar(
        x=ps.index,
        y=ps["Points"],
        name="Taškai"
    )
    data = Data([points])
    layout = Layout(title="Žaidėjų taškai")
    figure = Figure(data=data, layout=layout)
    py.plot(figure, filename="Player Points", auto_open=False)


def calculate_points(player, total, winners):
    if player in winners:
        return int(2520 * len(total) / len(winners)) - 2520
    return -2520


def role_points():
    df = pd.DataFrame(
        [
            (role, calculate_points(role, game.roles, game.winner_roles))
            for game in db.load()
            for role in game.roles
        ],
        columns=["Role", "Points"]
    ).groupby("Role").filter(lambda x: len(x) > 5).groupby("Role")

    df = df.sum() / df.count()

    return ((df - df.min()) / (df.max() - df.min()) * 100) \
        .astype("int").sort("Points", ascending=0)


def role_points_plot():
    ps = role_points()
    points = Bar(
        x=ps.index,
        y=ps["Points"],
        name="Taškai"
    )
    data = Data([points])
    layout = Layout(title="Rolių taškai")
    figure = Figure(data=data, layout=layout)
    py.plot(figure, filename="Role Points", auto_open=False)


players = player_points_plot
roles = role_points_plot