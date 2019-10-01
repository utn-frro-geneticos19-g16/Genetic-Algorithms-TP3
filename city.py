#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Every City for the Cities Manager's Cities List
class City(object):
    def __init__(self, name, cities_neig, lat, long):
        self.name = name
        self.neig = cities_neig
        self.lat = lat
        self.lng = long

    # Shows the Nearest City among all
    def get_nearest_neig(self, visited_cities):
        # List Comprehension (and Lambda Expression) for Nearest City
        nearest_city = min({x for x in self.neig.items() if x[0] not in visited_cities},
                           key=lambda x: x[1])

        return {
            "name": nearest_city[0],
            "distance": nearest_city[1]
        }

    # Get a Distance between the actual City and another one
    def get_distance_to(self, city):
        return self.neig[city.get_name()]

    def get_name(self):
        return self.name

    def get_lat(self):
        return self.lat

    def get_lng(self):
        return self.lng
