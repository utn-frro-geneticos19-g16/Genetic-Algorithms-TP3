from typing import List

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/Map')
def show_map():
    cities_list = ["Santa Fe", "La Plata", "Cordoba"]

    return render_template("showMap.html", cities_list=cities_list)


if __name__ == '__main__':
    app.run()
