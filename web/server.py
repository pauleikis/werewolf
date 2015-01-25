#!/usr/bin/env python
from ext.angular import AngularFlask
from ww.index import ww


app = AngularFlask(__name__)
app.config.from_pyfile('config/default.cfg')
app.config.from_envvar('WEREWOLF_SETTINGS', silent=True)
app.config.from_envvar('FLASK_SECRET')

app.register_blueprint(ww)

if __name__ == "__main__":
    app.run(host="0.0.0.0")