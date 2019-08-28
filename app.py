from typing import List
import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/Map')
def show_map():
    cities = [{"nombre": "Santa Fe"}, {"nombre": "La Plata"}, {"nombre": "Cordoba"}]

    return render_template("showMap.html", cities=cities)


if __name__ == '__main__':
    app.run()
