#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TP3: TRAVELING SALESMAN PROBLEM - ENUNCIADO:

1. Hallar la ruta de distancia mínima que logre unir todas las capitales de provincias de la República Argentina,
utilizando un método exhaustivo. ¿Puede resolver el problema? Justificar de manera teórica.

2. Realizar un programa que cuente con un menú con las siguientes opciones:
    a) Permitir ingresar una provincia y hallar la ruta de distancia mínima que logre unir todas las capitales de
    provincias de la República Argentina partiendo de dicha capital utilizando la siguiente heurística:
    "Desde cada ciudad ir a la ciudad más cercana no visitada". Recordar regresar siempre a la ciudad de partida.
    Presentar un mapa de la República con el recorrido indicado. Además indicar la ciudad de partida, el recorrido
    completo y la longitud del trayecto. El programa deberá permitir seleccionar la capital que el usuario desee
    ingresar como inicio del recorrido.

    b) Encontrar el recorrido mínimo para visitar todas las capitales de las provincias de la República Argentina
    siguiendo la heurística mencionada en el punto a. Deberá mostrar como salida recorrido y longitud del trayecto.

    c) Hallar la ruta de distancia mínima que logre unir todas las capitales de provincias de la República Argentina,
    utilizando un algoritmo genético.

FECHA DE ENTREGA: 30/09/2019

--> Genetic-Algorithm TP3 --- V1.0 ---  Created on 3 sep. 2019

            Antonelli, Nicolás - Recalde, Alejando - Rohn, Alex
"""

from flask import Flask
from flask import render_template
from citiesManager import CitiesManager

# App Initialization
app = Flask(__name__)

# Cities Initialization
cities = CitiesManager()


# Index
@app.route('/')
def hello_world():
    print("llego a menu inicio")
    return render_template("index.html")


# Best Track starting from a Selected City
@app.route('/Map/<root_city_name>')
def show_track_from(root_city_name):
    print("Llego a show_track_from, ciudad_origen: " + root_city_name)
    track = cities.get_best_track_from(root_city_name)

    print(track)

    return render_template("showMap.html", track=track)


# Best Track of all Tracks
@app.route('/Map')
def show_best_track():
    best_track = cities.get_best_track()

    return render_template("showMap.html", track=best_track)


# Best Track Using Genetic Algorithm
@app.route('/Map/Ag')
def show_track_with_ag():
    track_ag = cities.get_track_with_ag()

    return render_template("showMap.html", track=track_ag)


# Main Function
if __name__ == '__main__':
    app.run()
