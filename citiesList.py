from neighbourCitiesRepo import NeighbourCitiesRepo
from city import City
from cityToVisit import CityToVisit


class CitiesList(object):
    def __init__(self):
        self.citiesRepo = NeighbourCitiesRepo()

        buenos_aires = City(name="Buenos Aires"
                            , cities_neig=self.citiesRepo.get_near_cities_dict("Buenos Aires")
                            , long=588, lat=487)
        la_plata = City(name="La Plata"
                        , cities_neig=self.citiesRepo.get_near_cities_dict("La Plata")
                        , long=247, lat=460)
        cordoba = City(name="Cordoba"
                       , cities_neig=self.citiesRepo.get_near_cities_dict("Cordoba")
                       , long=800, lat=495)
        santa_fe = City(name="Santa Fe"
                        , cities_neig=self.citiesRepo.get_near_cities_dict("Santa Fe")
                        , long=975, lat=354)
        self.cities = {
            "Buenos Aires": buenos_aires
            , "La Plata": la_plata
            , "Cordoba": cordoba
            , "Santa Fe": santa_fe
        }

    def get_best_track_from(self, root_city_name):
        root_city = CityToVisit(
            name=self.cities[root_city_name].get_name()
            , lat=self.cities[root_city_name].get_lat()
            , long=self.cities[root_city_name].get_long())

        visited_cities = [root_city]
        accumulated_distance = 0

        while len(visited_cities) <= len(self.cities):
            last_city = self.cities[visited_cities[-1].get_name()]

            if len(visited_cities) == len(self.cities):
                accumulated_distance = accumulated_distance + last_city.get_distance_to(root_city)
                visited_cities.append(root_city)
            else:
                nearest_neig = last_city.get_nearest_neig([c.name for c in visited_cities])
                visited_cities.append(CityToVisit(
                    name=self.cities[nearest_neig["name"]].get_name()
                    , lat=self.cities[nearest_neig["name"]].get_lat()
                    , long=self.cities[nearest_neig["name"]].get_long())
                )
                accumulated_distance = accumulated_distance + nearest_neig["distance"]

        # https://stackoverflow.com/questions/21411497/flask-jsonify-a-list-of-objects
        return {
            "cities_to_visit": [c.serialize() for c in visited_cities]
            , "accumulated_distance": accumulated_distance
        }

    def get_best_track(self):
        best_track = self.get_best_track_from(list(self.cities)[0])

        for c in self.cities:
            track = self.get_best_track_from(c)
            if track["accumulated_distance"] < best_track["accumulated_distance"]:
                best_track = track

        return best_track
