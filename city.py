class City(object):
    def __init__(self, name, cities_neig, lat, long):
        self.name = name
        self.neig = cities_neig
        self.lat = lat
        self.long = long

    def get_nearest_neig(self, visited_cities):
        nearest_city = min({x for x in self.neig.items()
                            if x[0] not in visited_cities}
                           , key=lambda x: x[1])
        return nearest_city[0]

    def get_name(self):
        return self.name

    def get_lat(self):
        return self.lat

    def get_long(self):
        return self.long
