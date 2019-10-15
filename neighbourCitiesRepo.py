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
                             "S.M. de Tucuman": 1080, "S.S. de Jujuy": 1134, "Salta": 1282, "San Juan": 1005,
                             "San Luis": 749, "Santa Fe": 393, "Santa Rosa": 579, "Sgo. del Estero": 939,
                             "Ushuaia": 2373, "Viedma": 799},

            "Cordoba": {"Buenos Aires": 646, "Corrientes": 677, "Formosa": 824, "La Plata": 698, "La Rioja": 340,
                        "Mendoza": 466, "Neuquen": 907, "Parana": 348, "Posadas": 919, "Rawson": 1321,
                        "Resistencia": 669, "Rio Gallegos": 2281, "S.F.d.V.d. Catamarca": 362,
                        "S.M. de Tucuman": 517, "S.S. de Jujuy": 809, "Salta": 745, "San Juan": 412,
                        "San Luis": 293, "Santa Fe": 330, "Santa Rosa": 577, "Sgo. del Estero": 401,
                        "Ushuaia": 2618, "Viedma": 1047},

            "Corrientes": {"Buenos Aires": 792, "Cordoba": 677, "Formosa": 157, "La Plata": 830, "La Rioja": 814,
                           "Mendoza": 1131, "Neuquen": 1534, "Parana": 500, "Posadas": 291, "Rawson": 1845,
                           "Resistencia": 13, "Rio Gallegos": 2819, "S.F.d.V.d. Catamarca": 691,
                           "S.M. de Tucuman": 633, "S.S. de Jujuy": 742, "Salta": 719, "San Juan": 1039,
                           "San Luis": 969, "Santa Fe": 498, "Santa Rosa": 1136, "Sgo. del Estero": 535,
                           "Ushuaia": 3131, "Viedma": 1527},

            "Formosa": {"Buenos Aires": 933, "Cordoba": 824, "Corrientes": 157, "La Plata": 968, "La Rioja": 927,
                        "Mendoza": 1269, "Neuquen": 1690, "Parana": 656, "Posadas": 263, "Rawson": 1999,
                        "Resistencia": 161, "Rio Gallegos": 2974, "S.F.d.V.d. Catamarca": 793,
                        "S.M. de Tucuman": 703, "S.S. de Jujuy": 750, "Salta": 741, "San Juan": 1169,
                        "San Luis": 1117, "Santa Fe": 654, "Santa Rosa": 1293, "Sgo. del Estero": 629,
                        "Ushuaia": 3284, "Viedma": 1681},

            "La Plata": {"Buenos Aires": 53, "Cordoba": 698, "Corrientes": 830, "Formosa": 968, "La Rioja": 1038,
                         "Mendoza": 1029, "Neuquen": 1005, "Parana": 427, "Posadas": 857, "Rawson": 1116,
                         "Resistencia": 883, "Rio Gallegos": 2064, "S.F.d.V.d. Catamarca": 1030,
                         "S.M. de Tucuman": 1132, "S.S. de Jujuy": 1385, "Salta": 1333, "San Juan": 1053,
                         "San Luis": 795, "Santa Fe": 444, "Santa Rosa": 602, "Sgo. del Estero": 991,
                         "Ushuaia": 2350, "Viedma": 789},

            "La Rioja": {"Buenos Aires": 986, "Cordoba": 340, "Corrientes": 814, "Formosa": 927, "La Plata": 1038,
                         "Mendoza": 427, "Neuquen": 1063, "Parana": 659, "Posadas": 1098, "Rawson": 1548,
                         "Resistencia": 802, "Rio Gallegos": 2473, "S.F.d.V.d. Catamarca": 149,
                         "S.M. de Tucuman": 330, "S.S. de Jujuy": 600, "Salta": 533, "San Juan": 283,
                         "San Luis": 435, "Santa Fe": 640, "Santa Rosa": 834, "Sgo. del Estero": 311,
                         "Ushuaia": 2821, "Viedma": 1311},

            "Mendoza": {"Buenos Aires": 985, "Cordoba": 466, "Corrientes": 1131, "Formosa": 1269, "La Plata": 1029,
                        "La Rioja": 427, "Neuquen": 676, "Parana": 790, "Posadas": 1384, "Rawson": 1201,
                        "Resistencia": 1121, "Rio Gallegos": 2081, "S.F.d.V.d. Catamarca": 569,
                        "S.M. de Tucuman": 756, "S.S. de Jujuy": 1023, "Salta": 957, "San Juan": 152,
                        "San Luis": 235, "Santa Fe": 775, "Santa Rosa": 586, "Sgo. del Estero": 713,
                        "Ushuaia": 2435, "Viedma": 1019},

            "Neuquen": {"Buenos Aires": 989, "Cordoba": 907, "Corrientes": 1534, "Formosa": 1690, "La Plata": 1005,
                        "La Rioja": 1063, "Mendoza": 676, "Parana": 1053, "Posadas": 1709, "Rawson": 543,
                        "Resistencia": 1529, "Rio Gallegos": 1410, "S.F.d.V.d. Catamarca": 1182,
                        "S.M. de Tucuman": 1370, "S.S. de Jujuy": 1658, "Salta": 1591, "San Juan": 824,
                        "San Luis": 643, "Santa Fe": 1049, "Santa Rosa": 422, "Sgo. del Estero": 1286,
                        "Ushuaia": 1762, "Viedma": 479},

            "Parana": {"Buenos Aires": 375, "Cordoba": 348, "Corrientes": 500, "Formosa": 656, "La Plata": 427,
                       "La Rioja": 659, "Mendoza": 790, "Neuquen": 1053, "Posadas": 658, "Rawson": 1345,
                       "Resistencia": 498, "Rio Gallegos": 2230, "S.F.d.V.d. Catamarca": 622,
                       "S.M. de Tucuman": 707, "S.S. de Jujuy": 659, "Salta": 906, "San Juan": 757,
                       "San Luis": 574, "Santa Fe": 19, "Santa Rosa": 642, "Sgo. del Estero": 566,
                       "Ushuaia": 2635, "Viedma": 1030},

            "Posadas": {"Buenos Aires": 834, "Cordoba": 919, "Corrientes": 291, "Formosa": 263, "La Plata": 857,
                        "La Rioja": 1098, "Mendoza": 1384, "Neuquen": 1709, "Parana": 658, "Rawson": 1951,
                        "Resistencia": 305, "Rio Gallegos": 2914, "S.F.d.V.d. Catamarca": 980,
                        "S.M. de Tucuman": 924, "S.S. de Jujuy": 1007, "Salta": 992, "San Juan": 1306,
                        "San Luis": 1200, "Santa Fe": 664, "Santa Rosa": 1293, "Sgo. del Estero": 827,
                        "Ushuaia": 3207, "Viedma": 1624},

            "Rawson": {"Buenos Aires": 1127, "Cordoba": 1321, "Corrientes": 1845, "Formosa": 1999, "La Plata": 1116,
                       "La Rioja": 1548, "Mendoza": 1201, "Neuquen": 543, "Parana": 1345, "Posadas": 1951,
                       "Resistencia": 1843, "Rio Gallegos": 975, "S.F.d.V.d. Catamarca": 1647,
                       "S.M. de Tucuman": 1827, "S.S. de Jujuy": 2120, "Salta": 2054, "San Juan": 1340,
                       "San Luis": 1113, "Santa Fe": 1349, "Santa Rosa": 745, "Sgo. del Estero": 1721,
                       "Ushuaia": 1300, "Viedma": 327},

            "Resistencia": {"Buenos Aires": 794, "Cordoba": 669, "Corrientes": 13, "Formosa": 161, "La Plata": 833,
                            "La Rioja": 802,
                            "Mendoza": 1121, "Neuquen": 1529, "Parana": 498, "Posadas": 305, "Rawson": 1843,
                            "Rio Gallegos": 2818, "S.F.d.V.d. Catamarca": 678,
                            "S.M. de Tucuman": 620, "S.S. de Jujuy": 729, "Salta": 706, "San Juan": 1029,
                            "San Luis": 961, "Santa Fe": 495, "Santa Rosa": 1132, "Sgo. del Estero": 523,
                            "Ushuaia": 3130, "Viedma": 1526},

            "Rio Gallegos": {"Buenos Aires": 2082, "Cordoba": 2281, "Corrientes": 2819, "Formosa": 2974,
                             "La Plata": 2064, "La Rioja": 2473, "Mendoza": 2081, "Neuquen": 1410, "Parana": 2320,
                             "Posadas": 2914, "Rawson": 975, "Resistencia": 2818, "S.F.d.V.d. Catamarca": 2587,
                             "S.M. de Tucuman": 2773, "S.S. de Jujuy": 3063, "Salta": 2997, "San Juan": 2231,
                             "San Luis": 2046, "Santa Fe": 2325, "Santa Rosa": 1712, "Sgo. del Estero": 2677,
                             "Ushuaia": 359, "Viedma": 1294},

            "S.F.d.V.d. Catamarca": {"Buenos Aires": 979, "Cordoba": 362, "Corrientes": 691, "Formosa": 793,
                                     "La Plata": 1030, "La Rioja": 149, "Mendoza": 569, "Neuquen": 1182, "Parana": 622,
                                     "Posadas": 980, "Rawson": 1647, "Resistencia": 678, "Rio Gallegos": 2587,
                                     "S.M. de Tucuman": 189, "S.S. de Jujuy": 477, "Salta": 410, "San Juan": 430,
                                     "San Luis": 540, "Santa Fe": 689, "Santa Rosa": 1088, "Sgo. del Estero": 166,
                                     "Ushuaia": 3116, "Viedma": 1562},

            "S.M. de Tucuman": {"Buenos Aires": 1080, "Cordoba": 517, "Corrientes": 633, "Formosa": 703,
                                "La Plata": 1132, "La Rioja": 330, "Mendoza": 756, "Neuquen": 1370, "Parana": 707,
                                "Posadas": 924, "Rawson": 1827, "Resistencia": 620, "Rio Gallegos": 2773,
                                "S.F.d.V.d. Catamarca": 189, "S.S. de Jujuy": 293, "Salta": 228, "San Juan": 612,
                                "San Luis": 727, "Santa Fe": 689, "Santa Rosa": 1088, "Sgo. del Estero": 141,
                                "Ushuaia": 3116, "Viedma": 1562},

            "S.S. de Jujuy": {"Buenos Aires": 1334, "Cordoba": 809, "Corrientes": 742, "Formosa": 750,
                               "La Plata": 1385, "La Rioja": 600, "Mendoza": 1023, "Neuquen": 1658, "Parana": 959,
                               "Posadas": 1007, "Rawson": 2120, "Resistencia": 729, "Rio Gallegos": 3063,
                               "S.F.d.V.d. Catamarca": 477, "S.M. de Tucuman": 293, "Salta": 67, "San Juan": 874,
                               "San Luis": 1017, "Santa Fe": 942, "Santa Rosa": 1382, "Sgo. del Estero": 414,
                               "Ushuaia": 3408, "Viedma": 1855},

            "Salta": {"Buenos Aires": 1282, "Cordoba": 745, "Corrientes": 719, "Formosa": 741, "La Plata": 1333,
                      "La Rioja": 233, "Mendoza": 957, "Neuquen": 1591, "Parana": 906, "Posadas": 992, "Rawson": 2054,
                      "Resistencia": 706, "Rio Gallegos": 2997, "S.F.d.V.d. Catamarca": 410,
                      "S.M. de Tucuman": 228, "S.S. de Jujuy": 67, "San Juan": 808,
                      "San Luis": 950, "Santa Fe": 889, "Santa Rosa": 1316, "Sgo. del Estero": 353,
                      "Ushuaia": 3341, "Viedma": 1790},

            "San Juan": {"Buenos Aires": 1005, "Cordoba": 412, "Corrientes": 1039, "Formosa": 1169, "La Plata": 1053,
                         "La Rioja": 283, "Mendoza": 152, "Neuquen": 824, "Parana": 757, "Posadas": 1306, "Rawson": 1340,
                         "Resistencia": 1029, "Rio Gallegos": 2231, "S.F.d.V.d. Catamarca": 430,
                         "S.M. de Tucuman": 612, "S.S. de Jujuy": 874, "Salta": 808,
                         "San Luis": 284, "Santa Fe": 740, "Santa Rosa": 686, "Sgo. del Estero": 583,
                         "Ushuaia": 2585, "Viedma": 1141},

            "San Luis": {"Buenos Aires": 749, "Cordoba": 293, "Corrientes": 969, "Formosa": 1117, "La Plata": 795,
                         "La Rioja": 435, "Mendoza": 235, "Neuquen": 643, "Parana": 574, "Posadas": 1200, "Rawson": 1113,
                         "Resistencia": 961, "Rio Gallegos": 2046, "S.F.d.V.d. Catamarca": 540,
                         "S.M. de Tucuman": 727, "S.S. de Jujuy": 1017, "Salta": 950, "San Juan": 284,
                         "Santa Fe": 560, "Santa Rosa": 412, "Sgo. del Estero": 643, "Ushuaia": 2392, "Viedma": 882},

            "Santa Fe": {"Buenos Aires": 393, "Cordoba": 330, "Corrientes": 498, "Formosa": 654, "La Plata": 444,
                         "La Rioja": 640,
                         "Mendoza": 775, "Neuquen": 1049, "Parana": 19, "Posadas": 664, "Rawson": 1349,
                         "Resistencia": 495, "Rio Gallegos": 2325, "S.F.d.V.d. Catamarca": 602,
                         "S.M. de Tucuman": 689, "S.S. de Jujuy": 942, "Salta": 889, "San Juan": 740,
                         "San Luis": 560, "Santa Rosa": 641, "Sgo. del Estero": 547,
                         "Ushuaia": 2641, "Viedma": 1035},

            "Santa Rosa": {"Buenos Aires": 579, "Cordoba": 577, "Corrientes": 1136, "Formosa": 1293, "La Plata": 602,
                           "La Rioja": 834,
                           "Mendoza": 586, "Neuquen": 422, "Parana": 642, "Posadas": 1293, "Rawson": 745,
                           "Resistencia": 1132, "Rio Gallegos": 1712, "S.F.d.V.d. Catamarca": 915,
                           "S.M. de Tucuman": 1088, "S.S. de Jujuy": 1382, "Salta": 1316, "San Juan": 686,
                           "San Luis": 412, "Santa Fe": 641, "Sgo. del Estero": 977,
                           "Ushuaia": 2044, "Viedma": 477},

            "Sgo. del Estero": {"Buenos Aires": 979, "Cordoba": 401, "Corrientes": 535, "Formosa": 629, "La Plata": 991,
                                "La Rioja": 311,
                                "Mendoza": 713, "Neuquen": 1286, "Parana": 566, "Posadas": 827, "Rawson": 1721,
                                "Resistencia": 523, "Rio Gallegos": 2677, "S.F.d.V.d. Catamarca": 166,
                                "S.M. de Tucuman": 141, "S.S. de Jujuy": 414, "Salta": 353, "San Juan": 583,
                                "San Luis": 643, "Santa Fe": 547, "Santa Rosa": 977,
                                "Ushuaia": 3016, "Viedma": 1446},

            "Ushuaia": {"Buenos Aires": 2373, "Cordoba": 2618, "Corrientes": 3131, "Formosa": 3284, "La Plata": 2350,
                        "La Rioja": 2821, "Mendoza": 2435, "Neuquen": 1762, "Parana": 2635, "Posadas": 3207,
                        "Rawson": 1300, "Resistencia": 3130, "Rio Gallegos": 359, "S.F.d.V.d. Catamarca": 2931,
                        "S.M. de Tucuman": 3116, "S.S. de Jujuy": 3408, "Salta": 3341, "San Juan": 2585,
                        "San Luis": 2392, "Santa Fe": 2641, "Santa Rosa": 2044, "Sgo. del Estero": 3016,
                        "Viedma": 1605},

            "Viedma": {"Buenos Aires": 799, "Cordoba": 1047, "Corrientes": 1527, "Formosa": 1681, "La Plata": 789,
                       "La Rioja": 1311, "Mendoza": 1019, "Neuquen": 479, "Parana": 1030, "Posadas": 1624, "Rawson": 327,
                       "Resistencia": 1526, "Rio Gallegos": 1294, "S.F.d.V.d. Catamarca": 1391,
                       "S.M. de Tucuman": 1562, "S.S. de Jujuy": 1855, "Salta": 1790, "San Juan": 1141,
                       "San Luis": 882, "Santa Fe": 1035, "Santa Rosa": 477, "Sgo. del Estero": 1446,
                       "Ushuaia": 1605},

            # More 16 Cities like "Santa Fe": {"Buenos Aires": 4, "La Plata": 5, "Cordoba": 13},
        }

    # Get one City element of the Dictionary
    def get_near_cities_dict(self, city):
        return self.cities[city]
