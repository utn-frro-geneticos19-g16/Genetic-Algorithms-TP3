from typing import List, Dict
import json
import operator
import city
import citiesDictionaryRepo

from flask import Flask, render_template

app = Flask(__name__)

citiesRepo = citiesDictionaryRepo.CitiesDictionaryRepo()

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
    citiesDict = {
        "Buenos Aires": buenos_aires
        , "La Plata": la_plata
        , "Cordoba": cordoba
        , "Santa Fe": santa_fe
    }

    # Test: Continue with this approach
    visited_cities = ["Cordoba"]

    while len(visited_cities) < 4:
        last_city = citiesDict[visited_cities[-1]]

        nearest_neig = last_city.get_nearest_neig(visited_cities)
        visited_cities.append(nearest_neig[0])

    print(visited_cities)

    return render_template("showMap.html", cities=visited_cities)


if __name__ == '__main__':
    app.run()

# min({x for x in v.items() if x[0] not in visited_cities}, key=lambda x: x[1])
# : [cordoba.get_lat(), cordoba.get_long()]