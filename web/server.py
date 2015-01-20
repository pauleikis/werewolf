from flask import Flask
from ww.index import ww


app = Flask(__name__)
app.register_blueprint(ww)

if __name__ == "__main__":
    app.run(host="10.0.1.8", debug=True)