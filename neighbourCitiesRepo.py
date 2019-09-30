class NeighbourCitiesRepo(object):
    def __init__(self):
        self.cities = {
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

    def get_near_cities_dict(self, city):
        return self.cities[city]
