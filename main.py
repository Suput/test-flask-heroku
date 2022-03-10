from flask import Flask, redirect
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    return redirect("/index")


@app.route("/index")
def index1():
    return "<h1>Новый текст</h1>"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
