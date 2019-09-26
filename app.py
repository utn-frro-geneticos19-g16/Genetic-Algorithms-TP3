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
            "La Plata": 3,
            "Santa Fe": 13
        }
    }

    # Test: Continue with this approach
    visited_cities = ["Cordoba"]

    while len(visited_cities) < 4:
        v = cities[visited_cities[-1]]

        print(min({x for x in v.items() if x[0] not in visited_cities}, key=lambda x: x[1]))

        nearest_neig = min({x for x in v.items() if x[0] not in visited_cities}, key=lambda x: x[1])
        visited_cities.append(nearest_neig[0])

    return render_template("showMap.html", cities=visited_cities)


if __name__ == '__main__':
    app.run()
