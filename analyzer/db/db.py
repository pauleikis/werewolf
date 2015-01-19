import pickle

from model.game import Game


def save(obj):
    with open("data/data.db", "wb") as out:
        pickle.dump(obj, out)


def load():
    with open("data/data.db", "rb") as inp:
        return pickle.load(inp)


def update():
    save(list(games()))


def games():
    import os; print(os.getcwd())
    collected = ""
    for line in open("data/ww.dat"):
        if not line.strip():
            yield Game(collected)
            collected = ""
        else:
            collected += line
    if collected:
        yield Game(collected)