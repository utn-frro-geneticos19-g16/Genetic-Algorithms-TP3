from typing import List
import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/Map')
def show_map():
    cities = [
        {"nombre": "Santa Fe", "posX": "0090", "posY": "0100"},
        {"nombre": "Buenos Aires", "posX": "0021", "posY": "0030"},
        {"nombre": "La Plata", "posX": "0040", "posY": "0040"},
        {"nombre": "Cordoba", "posX": "0101", "posY": "0078"},
    ]

    return render_template("showMap.html", cities=cities)


if __name__ == '__main__':
    app.run()
