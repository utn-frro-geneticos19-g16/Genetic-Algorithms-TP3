#!/usr/bin/env python
# -*- coding: utf-8 -*-

from neighbourCitiesRepo import NeighbourCitiesRepo
from city import City
from cityToVisit import CityToVisit
# Genetic Algorithm...


# Initialization of All Cities
class CitiesManager(object):
    def __init__(self):
        self.citiesRepo = NeighbourCitiesRepo()

        # FIX: Long and Lat...
        # Completar...

        buenos_aires = City(name="Buenos Aires", cities_neig=self.citiesRepo.get_near_cities_dict("Buenos Aires"),
                            long=588, lat=487)

        cordoba = City(name="Cordoba", cities_neig=self.citiesRepo.get_near_cities_dict("Cordoba"),
                       long=800, lat=495)

        corrientes = City(name="Corrientes", cities_neig=self.citiesRepo.get_near_cities_dict("Corrientes"),
                       long=1001, lat=1001)

        formosa = City(name="Formosa", cities_neig=self.citiesRepo.get_near_cities_dict("Formosa"),
                       long=1001, lat=1001)

        la_plata = City(name="La Plata", cities_neig=self.citiesRepo.get_near_cities_dict("La Plata"),
                        long=247, lat=460)

        la_rioja = City(name="La Rioja", cities_neig=self.citiesRepo.get_near_cities_dict("La Rioja"),
                        long=1001, lat=1001)

        mendoza = City(name="Mendoza", cities_neig=self.citiesRepo.get_near_cities_dict("Mendoza"),
                        long=1001, lat=1001)

        neuquen = City(name="Neuquen", cities_neig=self.citiesRepo.get_near_cities_dict("Neuquen"),
                        long=1001, lat=1001)

        # More 16 Cities Like Santa Fe
        # santa_fe = City(name="Santa Fe", cities_neig=self.citiesRepo.get_near_cities_dict("Santa Fe"),
                        # long=975, lat=354)

        # Dictionary with all City Objects
        self.cities = {
            "Buenos Aires": buenos_aires,
            "Cordoba": cordoba,
            "Corrientes": corrientes,
            "Formosa": formosa,
            "La Plata": la_plata,
            "La Rioja": la_rioja,
            "Mendoza": mendoza,
            "Neuquen": neuquen,
            # "Santa Fe": santa_fe...
        }

    # Best Track starting with a Selected One
    def get_best_track_from(self, root_city_name):

        # Create a "CityToVisit" object for Every city on the travel
        root_city = CityToVisit(
            name=self.cities[root_city_name].get_name(),
            lat=self.cities[root_city_name].get_lat(),
            long=self.cities[root_city_name].get_long())

        # All CityToVisit List and Total Travel Distance
        visited_cities = [root_city]
        accumulated_distance = 0

        # The List of Visited Cities must have the same length of all "Cities" list
        while len(visited_cities) <= len(self.cities):
            last_city = self.cities[visited_cities[-1].get_name()]

            # On the last Loop: Go back to the Start City
            if len(visited_cities) == len(self.cities):
                accumulated_distance = accumulated_distance + last_city.get_distance_to(root_city)
                visited_cities.append(root_city)
            else:
                # Check that the next nearest city is not in the List of Visited Cities
                nearest_neig = last_city.get_nearest_neig([c.name for c in visited_cities])
                # Add the new City on the Visited Cities List
                visited_cities.append(CityToVisit(
                    name=self.cities[nearest_neig["name"]].get_name(),
                    lat=self.cities[nearest_neig["name"]].get_lat(),
                    long=self.cities[nearest_neig["name"]].get_long())
                )
                # Update Total Distance
                accumulated_distance = accumulated_distance + nearest_neig["distance"]

        # https://stackoverflow.com/questions/21411497/flask-jsonify-a-list-of-objects
        # Returns all cities on Visited Cities List (Serialized) and Total Distance
        return {
            "cities_to_visit": [c.serialize() for c in visited_cities],
            "accumulated_distance": accumulated_distance
        }

    # Best Track of all Tracks
    def get_best_track(self):
        # Get Best Track for the First existent City
        best_track = self.get_best_track_from(list(self.cities)[0])

        # Try every posible Track and Compare with the First One
        for c in self.cities:
            track = self.get_best_track_from(c)
            if track["accumulated_distance"] < best_track["accumulated_distance"]:
                best_track = track

        return best_track

    # Best Track Using Genetic Algorithm
    def get_track_with_ag(self):
        # Genethic Algorithm...
        pass
