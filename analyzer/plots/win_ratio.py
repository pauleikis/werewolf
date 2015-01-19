import pandas as pd
import plotly.plotly as py
from plotly.graph_objs import Bar, Layout, Data, Figure, Scatter, YAxis, Legend
from db import db


def players():
    reload_simple(player_simple, "player-simple", "Žaidėjai")


def roles():
    reload_simple(role_simple, "role-simple", "Rolės")


def reload_simple(data_function, doc, title):
    ps = data_function(db.load())

    played = Bar(
        x=ps.index,
        y=ps["Played"],
        name="Played"
    )
    won = Bar(
        x=ps.index,
        y=ps["Won"],
        name="Won"
    )
    winrate = Scatter(
        x=ps.index,
        y=ps["Winrate"],
        name="Winrate",
        yaxis="y2"
    )
    layout = Layout(
        barmode="overlay",
        yaxis2=YAxis(
            side="right",
            overlaying="y",
            title="Winrate [%]",
            range=[0, 100]
        ),
        legend=Legend(x=0, y=0),
        title=title
    )
    data = Data([played, won, winrate])
    figure = Figure(data=data, layout=layout)

    py.plot(figure, filename=doc, auto_open=False)


def player_simple(data):
    result = pd.DataFrame(
        [pd.DataFrame([x.players for x in data]).stack().value_counts(),
         pd.DataFrame([x.winners for x in data]).stack().value_counts()],
        index=["Played", "Won"]).T

    fill_winrate(result)
    return result.sort(["Winrate", "Played"], ascending=[0, 0])


def role_simple(data):
    result = pd.DataFrame(
        [
            pd.DataFrame([x.roles for x in data]).stack().value_counts(),
            pd.DataFrame([x.winner_roles for x in data]).stack().value_counts()
        ],
        index=["Played", "Won"]
    ).T

    fill_winrate(result)
    return result.sort(["Winrate", "Played"], ascending=[0, 0])


def fill_winrate(data):
    data["Winrate"] = (data["Won"].fillna(0) * 100 / data["Played"]) \
        .astype('int')
    return data