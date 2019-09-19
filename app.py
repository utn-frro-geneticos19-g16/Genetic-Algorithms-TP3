from typing import List, Dict
import json
import operator
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/Map')
def show_map():
    cities = {
        "Santa Fe": {
            "Buenos Aires": 4,
            "La Plata": 5,
            "Cordoba": 13
        },
        "Buenos Aires": {
            "Santa Fe": 4,
            "La Plata": 5,
            "Cordoba": 13
        },
        "La Plata": {
            "Buenos Aires": 4,
            "Santa Fe": 5,
            "Cordoba": 13
        },
        "Cordoba": {
            "Buenos Aires": 4,
            "La Plata": 5,
            "Santa Fe": 13
        }
    }

    # Test: Continue with this approach
    for k, v in cities.items():
        print(min(v.items(), key=lambda key: key[1]))

    return render_template("showMap.html", cities=cities)


if __name__ == '__main__':
    app.run()
