class CityToVisit(object):
    def __init__(self, name, lat, long):
        self.name = name
        self.lat = lat
        self.long = long

    def get_name(self):
        return self.name

    def get_lat(self):
        return self.lat

    def get_long(self):
        return self.long

    def serialize(self):
        return {
            "name": self.name
            , "lat": self.lat
            , "lng": self.long
        }
