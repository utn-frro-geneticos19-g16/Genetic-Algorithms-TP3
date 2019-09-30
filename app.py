from typing import List, Dict
import json
import operator
import city
import cityToVisit
import nearCitiesRepo

from flask import Flask, render_template

app = Flask(__name__)

citiesRepo = nearCitiesRepo.NearCitiesRepo()

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/Map')
def show_map():
    buenos_aires = city.City(name="Buenos Aires"
                             , cities_neig=citiesRepo.get_neighbour_dict("Buenos Aires")
                             , long=588, lat=487)
    la_plata = city.City(name="La Plata"
                         , cities_neig=citiesRepo.get_neighbour_dict("La Plata")
                         , long=247, lat=460)
    cordoba = city.City(name="Cordoba"
                        , cities_neig=citiesRepo.get_neighbour_dict("Cordoba")
                        , long=800, lat=495)
    santa_fe = city.City(name="Santa Fe"
                         , cities_neig=citiesRepo.get_neighbour_dict("Santa Fe")
                         , long=975, lat=354)
    cities = {
        "Buenos Aires": buenos_aires
        , "La Plata": la_plata
        , "Cordoba": cordoba
        , "Santa Fe": santa_fe
    }

    # Test: Continue with this approach
    visited_cities = [cityToVisit.CityToVisit(
        name=cities["Cordoba"].get_name()
        , lat=cities["Cordoba"].get_lat()
        , long=cities["Cordoba"].get_long())]

    while len(visited_cities) < len(cities):
        last_city = cities[visited_cities[-1].get_name()]

        nearest_neig = last_city.get_nearest_neig(visited_cities)
        visited_cities.append(cityToVisit.CityToVisit(
            name=cities[nearest_neig].get_name()
            , lat=cities[nearest_neig].get_lat()
            , long=cities[nearest_neig].get_long())
        )

    # https://stackoverflow.com/questions/21411497/flask-jsonify-a-list-of-objects
    serialized_cities_to_visit = [c.serialize() for c in visited_cities]

    return render_template("showMap.html", cities=serialized_cities_to_visit)


if __name__ == '__main__':
    app.run()