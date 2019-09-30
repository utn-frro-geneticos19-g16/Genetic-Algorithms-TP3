from typing import List, Dict
import json
import operator
from city import City
from cityToVisit import CityToVisit
from neighbourCitiesRepo import NeighbourCitiesRepo

from flask import Flask, render_template

app = Flask(__name__)


def initilize_cities():
    buenos_aires = City(name="Buenos Aires"
                        , cities_neig=citiesRepo.get_near_cities_dict("Buenos Aires")
                        , long=588, lat=487)
    la_plata = City(name="La Plata"
                    , cities_neig=citiesRepo.get_near_cities_dict("La Plata")
                    , long=247, lat=460)
    cordoba = City(name="Cordoba"
                        , cities_neig=citiesRepo.get_near_cities_dict("Cordoba")
                        , long=800, lat=495)
    santa_fe = City(name="Santa Fe"
                         , cities_neig=citiesRepo.get_near_cities_dict("Santa Fe")
                         , long=975, lat=354)
    return {
        "Buenos Aires": buenos_aires
        , "La Plata": la_plata
        , "Cordoba": cordoba
        , "Santa Fe": santa_fe
    }


citiesRepo = NeighbourCitiesRepo()
cities = initilize_cities()


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/Map/<root_city_name>')
def show_track_from(root_city_name):
    track = get_best_track_from(root_city_name)

    return render_template("showMap.html", track=track)


@app.route('/Map')
def show_best_track():
    best_track = get_best_track_from(list(cities)[0])

    for c in cities:
        track = get_best_track_from(c)
        if track["accumulated_distance"] < best_track["accumulated_distance"]:
            best_track = track

    return render_template("showMap.html", track=best_track)


def get_best_track_from(root_city_name):
    root_city = CityToVisit(
        name=cities[root_city_name].get_name()
        , lat=cities[root_city_name].get_lat()
        , long=cities[root_city_name].get_long())

    visited_cities = [root_city]
    accumulated_distance = 0

    while len(visited_cities) <= len(cities):
        last_city = cities[visited_cities[-1].get_name()]

        if len(visited_cities) == len(cities):
            accumulated_distance = accumulated_distance + last_city.get_distance_to(root_city)
            visited_cities.append(root_city)
        else:
            nearest_neig = last_city.get_nearest_neig([c.name for c in visited_cities])
            visited_cities.append(CityToVisit(
                name=cities[nearest_neig["name"]].get_name()
                , lat=cities[nearest_neig["name"]].get_lat()
                , long=cities[nearest_neig["name"]].get_long())
            )
            accumulated_distance = accumulated_distance + nearest_neig["distance"]

    # https://stackoverflow.com/questions/21411497/flask-jsonify-a-list-of-objects
    return {
        "cities_to_visit": [c.serialize() for c in visited_cities]
        , "accumulated_distance": accumulated_distance
    }


if __name__ == '__main__':
    app.run()
