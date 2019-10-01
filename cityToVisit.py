#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Every City of the Visited List
class CityToVisit(object):
    def __init__(self, name, lat, long):
        self.name = name
        self.lat = lat
        self.lng = long

    def get_name(self):
        return self.name

    def get_lat(self):
        return self.lat

    def get_lng(self):
        return self.lng

    def serialize(self):
        return {
            "name": self.name,
            "lat": self.lat,
            "lng": self.lng
        }
