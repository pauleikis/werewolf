from db import db
import pandas as pd
import plotly.plotly as py
from plotly.graph_objs import Bar, Layout, Data, Figure
from plots.win_ratio import fill_winrate


def plot():
    panel = team_vs_player_count()

    def data():
        for item in panel.items:
            yield Bar(
                x=panel[item].index,
                y=panel[item]["Winrate"],
                name=item
            )

    data = Data(list(data()))
    layout = Layout(title="Komandos vs Žaidėjų skaičius")
    figure = Figure(data=data, layout=layout)
    py.plot(figure, filename="Team vs Count", auto_open=False)


def team_vs_player_count():
    raw = db.load()
    teams = ["Villagers", "Werewolves", "Tanner"]
    panel = {}

    for team in teams:
        data = pd.DataFrame(
            [pd.DataFrame(len(x.players) for x in raw if
                          team in x.teams).stack().value_counts(),
             pd.DataFrame(len(x.players) for x in raw if
                          team in x.winner).stack().value_counts()],
            index=["Played", "Won"]).T
        fill_winrate(data)
        panel[team] = data

    return pd.Panel(panel, items=teams)