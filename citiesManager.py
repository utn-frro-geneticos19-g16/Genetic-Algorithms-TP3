#!/usr/bin/env python
# -*- coding: utf-8 -*-

from neighbourCitiesRepo import NeighbourCitiesRepo
from city import City
from cityToVisit import CityToVisit
from population import Population
from chromosome import Chromosome

# Initialization of All Cities
class CitiesManager(object):
    def __init__(self):
        self.citiesRepo = NeighbourCitiesRepo()

        buenos_aires = City(name="Buenos Aires", cities_neig=self.citiesRepo.get_near_cities_dict("Buenos Aires")
                            , lat=-34.6131516, long=-58.3772316,)

        cordoba = City(name="Cordoba", cities_neig=self.citiesRepo.get_near_cities_dict("Cordoba")
                       , lat=-31.4134998, long=-64.1810532)

        corrientes = City(name="Corrientes", cities_neig=self.citiesRepo.get_near_cities_dict("Corrientes")
                          , lat=-27.4806004, long=-58.8340988)

        formosa = City(name="Formosa", cities_neig=self.citiesRepo.get_near_cities_dict("Formosa")
                       , lat=-26.1775303, long=-58.1781387)

        la_plata = City(name="La Plata", cities_neig=self.citiesRepo.get_near_cities_dict("La Plata")
                        , lat=-34.9214516, long=-57.9545288)

        la_rioja = City(name="La Rioja", cities_neig=self.citiesRepo.get_near_cities_dict("La Rioja")
                        , lat=-29.4110508, long=-66.8506699)

        mendoza = City(name="Mendoza", cities_neig=self.citiesRepo.get_near_cities_dict("Mendoza")
                       , lat=-32.8908386, long=-68.8271713)

        neuquen = City(name="Neuquen", cities_neig=self.citiesRepo.get_near_cities_dict("Neuquen")
                       , lat=-38.9516106, long=-68.0590973)

        parana = City(name="Parana", cities_neig=self.citiesRepo.get_near_cities_dict("Parana")
                       , lat=-31.7319698, long=-60.5237999)

        posadas = City(name="Posadas", cities_neig=self.citiesRepo.get_near_cities_dict("Posadas")
                       , lat=-27.3670807, long=-55.89608)

        rawson = City(name="Rawson", cities_neig=self.citiesRepo.get_near_cities_dict("Rawson")
                       , lat=-43.3001595, long=-65.1022797)

        resistencia = City(name="Resistencia", cities_neig=self.citiesRepo.get_near_cities_dict("Resistencia")
                       , lat=-27.4605598, long=-58.9838905)

        rio_gallegos = City(name="Rio Gallegos", cities_neig=self.citiesRepo.get_near_cities_dict("Rio Gallegos")
                       , lat=-51.6226082, long=-69.218132)

        sfdvd_catamarca = City(name="S.F.d.V.d. Catamarca", cities_neig=self.citiesRepo.get_near_cities_dict("S.F.d.V.d. Catamarca")
                       , lat=-28.4695702, long=-65.7852402)

        sm_de_tucuman = City(name="S.M. de Tucuman", cities_neig=self.citiesRepo.get_near_cities_dict("S.M. de Tucuman")
                       , lat=-26.8241405, long=-65.2226028)

        ss_de_jujuy = City(name="S.S. de Jujuy", cities_neig=self.citiesRepo.get_near_cities_dict("S.S. de Jujuy")
                       , lat=-24.1945705, long=-65.2971191)

        salta = City(name="Salta", cities_neig=self.citiesRepo.get_near_cities_dict("Salta")
                       , lat=-24.7859001, long=-65.4116592)

        san_juan = City(name="San Juan", cities_neig=self.citiesRepo.get_near_cities_dict("San Juan")
                       , lat=-31.5375004, long=-68.5363922)

        san_luis = City(name="San Luis", cities_neig=self.citiesRepo.get_near_cities_dict("San Luis")
                       , lat=-33.2950096, long=-66.3356323)

        santa_fe = City(name="Santa Fe", cities_neig=self.citiesRepo.get_near_cities_dict("Santa Fe")
                       , lat=-31.6333294, long=-60.7000008)

        santa_rosa = City(name="Santa Rosa", cities_neig=self.citiesRepo.get_near_cities_dict("Santa Rosa")
                       , lat=-36.6166687, long=-64.2833328)

        sgo_del_estero = City(name="Sgo. del Estero", cities_neig=self.citiesRepo.get_near_cities_dict("Sgo. del Estero")
                       , lat=-27.7951107, long=-64.2614899)

        ushuaia = City(name="Ushuaia", cities_neig=self.citiesRepo.get_near_cities_dict("Ushuaia")
                       , lat=-54.7999992, long=-68.3000031)

        viedma = City(name="Viedma", cities_neig=self.citiesRepo.get_near_cities_dict("Viedma")
                       , lat=-40.8134499, long=-62.9966812)

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
            "Parana": parana,
            "Posadas": posadas,
            "Rawson": rawson,
            "Resistencia": resistencia,
            "Rio Gallegos": rio_gallegos,
            "S.F.d.V.d. Catamarca": sfdvd_catamarca,
            "S.M. de Tucuman": sm_de_tucuman,
            "S.S. de Jujuy": ss_de_jujuy,
            "Salta": salta,
            "San Juan": san_juan,
            "San Luis": san_luis,
            "Santa Fe": santa_fe,
            "Santa Rosa": santa_rosa,
            "Sgo. del Estero": sgo_del_estero,
            "Ushuaia": ushuaia,
            "Viedma": viedma,
        }
        print("Correct Initialization")

    # Best Track starting with a Selected One
    def get_best_track_from(self, root_city_name):
        print("Llego a get_best_track_from, parametro: " + root_city_name)
        print(self.cities[root_city_name].get_lat())
        # Create a "CityToVisit" object for Every city on the travel
        root_city = CityToVisit(
            name=self.cities[root_city_name].get_name(),
            lat=self.cities[root_city_name].get_lat(),
            long=self.cities[root_city_name].get_lng())

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
                    long=self.cities[nearest_neig["name"]].get_lng())
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
        # ImportantValues
        iterationLimit = 4  # 200  # Population Iterations
        initPopulationNum = 10  # 50  # Initial Population Size
        crossoverProb = 0.75  # Probability of CrossOver
        mutationProb = 0.05  # Probability of Mutation

        track_ag = None  # Initialization of Best Track
        km_ag = 0  # Initialization of Total Distance

        # Initialize Chromosome
        Chromosome.setCitiesDict(self.cities)

        # First Population
        pob = Population(initPopulationNum, list(self.cities.keys()), crossoverProb, mutationProb)

        # Iterations
        for iterationCount in range(iterationLimit):
            pob.showPopulation(iterationCount)

            # In the last iteration, the chromosomes population mustn't reproduce
            if iterationCount <= iterationLimit - 1:
                pob.reproduce()  # Reproduction of Actual Generation
                print("------------")

        # Last Reproduction Message
        print("Last Generation Reached Correctly")
        print("------------")
        print()
        print()

        # Get the Best Results after last generation
        track_ag, km_ag = pob.getBestTrackAg()

        # Convert track_ag in a citiesToVisit List
        track_ag_cities = []
        for i in range(track_ag):
            city_name = track_ag[i]
            track_ag_cities.append(CityToVisit(name=city_name, lat=self.cities[city_name].get_lat(),
                                               long=self.cities[city_name].get_lng()))

        print("track")
        print(track_ag)
        print("total: ", km_ag)

        return {
            "cities_to_visit": track_ag,
            "accumulated_distance": km_ag
        }
