from flask import Flask
from ww.index import ww


app = Flask(__name__)
app.config.from_pyfile('config/default.cfg')
app.config.from_envvar('WEREWOLF_SETTINGS', silent=True)

app.register_blueprint(ww)

if __name__ == "__main__":
    app.run(host="0.0.0.0")