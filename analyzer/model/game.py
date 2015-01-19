import configparser
import arrow

config = configparser.ConfigParser()
config.read("data/ww.ini")


def player(acronym):
    return config["Players"][acronym]


def role(acronym):
    return config["Roles"][acronym]


def team(acronym):
    if acronym in ["WW", "DW", "MW", "AW", "M"]:
        return "Werewolves"
    if acronym == "T":
        return "Tanner"
    return "Villagers"


class Game:

    def __init__(self, string):
        date, *participants = string.splitlines()
        participants = [x.upper().strip().split(":") for x in participants]

        self.date = arrow.get(date).format("YYYY-MM-DD")
        self.winners = [player(x[0]) for x in participants if x[3] == "W"]
        self.winner_roles = [role(x[1]) for x in participants if x[3] == "W"]
        self.players = [player(x[0]) for x in participants]
        self.roles = [role(x[1]) for x in participants]
        self.teams = {team(x[2]) for x in participants}
        self.winner = {team(x[2]) for x in participants if x[3] == "W"}

    def __str__(self):
        return str(vars(self))

    def __repr__(self):
        return str(self)
