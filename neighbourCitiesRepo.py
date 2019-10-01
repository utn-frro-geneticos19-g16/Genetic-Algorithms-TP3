#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Dictionary with all the Cities and Distances between all others
class NeighbourCitiesRepo(object):
    def __init__(self):
        # Completar...
        self.cities = {
            "Buenos Aires": {"Cordoba": 646, "Corrientes": 792, "Formosa": 933, "La Plata": 53, "La Rioja": 986,
                             "Mendoza": 985, "Neuquen": 989, "Parana": 375, "Posadas": 834, "Rawson": 1127,
                             "Resistencia": 794, "Rio Gallegos": 2082, "S.F.d.V.d. Catamarca": 979,
                             "S. M. de Tucuman": 1080, "S. S. de Jujuy": 1134, "Salta": 1282, "San Juan": 1005,
                             "San Luis": 749, "Santa Fe": 393, "Santa Rosa": 579, "Sgo. del Estero": 939,
                             "Ushuaia": 2373, "Viedma": 799},

            "Cordoba": {"Buenos Aires": 646, "Corrientes": 677, "Formosa": 824, "La Plata": 698, "La Rioja": 340,
                        "Mendoza": 466, "Neuquen": 907, "Parana": 348, "Posadas": 919, "Rawson": 1321,
                        "Resistencia": 669, "Rio Gallegos": 2281, "S.F.d.V.d. Catamarca": 362,
                        "S. M. de Tucuman": 517, "S. S. de Jujuy": 809, "Salta": 745, "San Juan": 412,
                        "San Luis": 293, "Santa Fe": 330, "Santa Rosa": 577, "Sgo. del Estero": 401,
                        "Ushuaia": 2618, "Viedma": 1047},

            "Corrientes": {"Buenos Aires": 792, "Cordoba": 677, "Formosa": 157, "La Plata": 830, "La Rioja": 814,
                           "Mendoza": 1131, "Neuquen": 1534, "Parana": 500, "Posadas": 291, "Rawson": 1845,
                           "Resistencia": 13, "Rio Gallegos": 2819, "S.F.d.V.d. Catamarca": 691,
                           "S. M. de Tucuman": 633, "S. S. de Jujuy": 742, "Salta": 719, "San Juan": 1039,
                           "San Luis": 969, "Santa Fe": 498, "Santa Rosa": 1136, "Sgo. del Estero": 535,
                           "Ushuaia": 3131, "Viedma": 1527},

            "Formosa": {"Buenos Aires": 933, "Cordoba": 824, "Corrientes": 157, "La Plata": 968, "La Rioja": 927,
                        "Mendoza": 1269, "Neuquen": 1690, "Parana": 656, "Posadas": 263, "Rawson": 1999,
                        "Resistencia": 161, "Rio Gallegos": 2974, "S.F.d.V.d. Catamarca": 793,
                        "S. M. de Tucuman": 703, "S. S. de Jujuy": 750, "Salta": 741, "San Juan": 1169,
                        "San Luis": 1117, "Santa Fe": 654, "Santa Rosa": 1293, "Sgo. del Estero": 629,
                        "Ushuaia": 3284, "Viedma": 1681},

            "La Plata": {"Buenos Aires": 53, "Cordoba": 698, "Corrientes": 830, "Formosa": 968, "La Rioja": 1038,
                         "Mendoza": 1029, "Neuquen": 1005, "Parana": 427, "Posadas": 857, "Rawson": 1116,
                         "Resistencia": 883, "Rio Gallegos": 2064, "S.F.d.V.d. Catamarca": 1030,
                         "S. M. de Tucuman": 1132, "S. S. de Jujuy": 1385, "Salta": 1333, "San Juan": 1053,
                         "San Luis": 795, "Santa Fe": 444, "Santa Rosa": 602, "Sgo. del Estero": 991,
                         "Ushuaia": 2350, "Viedma": 789},

            "La Rioja": {"Buenos Aires": 986, "Cordoba": 340, "Corrientes": 814, "Formosa": 927, "La Plata": 1038,
                         "Mendoza": 427, "Neuquen": 1063, "Parana": 659, "Posadas": 1098, "Rawson": 1548,
                         "Resistencia": 802, "Rio Gallegos": 2473, "S.F.d.V.d. Catamarca": 149,
                         "S. M. de Tucuman": 330, "S. S. de Jujuy": 600, "Salta": 533, "San Juan": 283,
                         "San Luis": 435, "Santa Fe": 640, "Santa Rosa": 834, "Sgo. del Estero": 311,
                         "Ushuaia": 2821, "Viedma": 1311},

            "Mendoza": {"Buenos Aires": 985, "Cordoba": 466, "Corrientes": 1131, "Formosa": 1269, "La Plata": 1029,
                        "La Rioja": 427, "Neuquen": 676, "Parana": 790, "Posadas": 1384, "Rawson": 1201,
                        "Resistencia": 1121, "Rio Gallegos": 2081, "S.F.d.V.d. Catamarca": 569,
                        "S. M. de Tucuman": 756, "S. S. de Jujuy": 1023, "Salta": 957, "San Juan": 152,
                        "San Luis": 235, "Santa Fe": 775, "Santa Rosa": 586, "Sgo. del Estero": 713,
                        "Ushuaia": 2435, "Viedma": 1019},

            "Neuquen": {"Buenos Aires": 989, "Cordoba": 907, "Corrientes": 1534, "Formosa": 1690, "La Plata": 1005,
                        "La Rioja": 1063, "Mendoza": 676, "Parana": 1053, "Posadas": 1709, "Rawson": 543,
                        "Resistencia": 1529, "Rio Gallegos": 1410, "S.F.d.V.d. Catamarca": 1182,
                        "S. M. de Tucuman": 1370, "S. S. de Jujuy": 1658, "Salta": 1591, "San Juan": 824,
                        "San Luis": 643, "Santa Fe": 1049, "Santa Rosa": 422, "Sgo. del Estero": 1286,
                        "Ushuaia": 1762, "Viedma": 479},

            # More 16 Cities like "Santa Fe": {"Buenos Aires": 4, "La Plata": 5, "Cordoba": 13},
        }

    # Get one City element of the Dictionary
    def get_near_cities_dict(self, city):
        return self.cities[city]
