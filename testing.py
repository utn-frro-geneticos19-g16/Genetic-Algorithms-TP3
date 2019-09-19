from tkinter import *
import pandas as pd
import random


class Cromosoma:
    id = -1
    fitness = -1
    cities = []

    def __init__(self, id=-1):
        self.fitness = 0
        self.cities = []
        self.id = id

    def __str__(self):
        return str(self.cities)

    def setFitness(self, allCities):

        beforeCity = None
        for city in self.cities:
            oCity = GetElement(allCities, city)

            if(beforeCity != None):
                distance = oCity.getDistance(beforeCity)
                self.fitness += distance

            beforeCity = oCity

        self.fitness = 10000 / self.fitness


class Distance:

    id = -1
    distance = -1

    def __init__(self, id, distance):
        self.id = id
        self.distance = distance


class City:

    id = -1
    name = ""
    relations = []
    x = -1
    y = -1

    def LoadDistances(self, cities):
        id = 0
        for distance in cities:
            self.relations.append(Distance(id, distance))

            id += 1

    def __init__(self, id, name, cities, x, y):
        self.id = id
        self.name = name

        self.relations = []
        self.LoadDistances(cities)
        self.relations.sort(key=lambda x: x.distance)

        self.x = x
        self.y = y

    def __str__(self):
        return self.name

    def GetNextCity(self, alreadyCities, allCities):
        for city in self.relations:
            if GetElement(alreadyCities, city.id) == None and city.distance != 0:

                return GetElement(allCities, city.id), city.distance

    def getDistance(self, oCity):
        for city in self.relations:
            if(oCity.id == city.id):
                return city.distance


def GetElement(array, id):
    for element in array:
        if(element.id == int(id)):
            return element

    return None


def DistanceOfProvince(cities, allCities, city=None, notExit=False):
    visitedCities = []

    if(city == None):
        print("----- Ingrese el codigo de la ciudad donde desea comenzar el recorrido -----")

        for city in cities:
            print(str(city.id) + " - " + city.name)

        input_city = input("¿En que ciuidad desea comenzar? ")
        startCity = GetElement(cities, input_city)

    else:
        startCity = city

    cities.remove(startCity)
    visitedCities.append(startCity)

    travelDistance = 0
    city = startCity
    while len(cities) != 0:
        nextCity = city.GetNextCity(visitedCities, allCities)
        visitedCities.append(nextCity[0])
        cities.remove(nextCity[0])
        city = nextCity[0]
        travelDistance += nextCity[1]

    visitedCities.append(startCity)

    if(notExit):
        return travelDistance

    root = Tk()
    canvas = Canvas(root, width = 373, height = 650)
    canvas.pack()
    img = PhotoImage(file="map.png")
    canvas.create_image(0, 0, anchor=NW, image=img)

    beforeCity = startCity
    for city in visitedCities:
        canvas.create_line(beforeCity.x, beforeCity.y, city.x, city.y, width=2, fill="red")
        beforeCity = city

    mainloop()

    print('Distancia total recorrida es: ' + str(travelDistance) + 'Km')


def MinimumDistance(allCities):

    bestFirstCity = None
    bestDistance = 100000

    for city in allCities:
        distance = DistanceOfProvince(allCities.copy(), allCities.copy(), city, True)

        if distance < bestDistance:
            bestFirstCity = city
            bestDistance = distance

    print("La mejor ciudad para comenzar es: " + str(bestFirstCity.name))
    DistanceOfProvince(allCities.copy(), allCities.copy(), bestFirstCity)


def crossover(cromoOne, cromoTwo, arraySons, allCities):
    sonOne = Cromosoma()
    sonTwo = Cromosoma()

    for x in range(0, 24):
        sonOne.cities.append(None)
        sonTwo.cities.append(None)


    sonOne.cities[0] = cromoOne.cities[0]
    aux = cromoTwo.cities[0]


    while aux != cromoOne.cities[0]:
        for x in range(0,24):
            if cromoOne.cities[x] == aux:
                sonOne.cities[x] = aux
                aux = cromoTwo.cities[x]


    for x in range(0,24):
        if sonOne.cities[x] is None:
            sonOne.cities[x] = cromoTwo.cities[x]


    #Second

    sonTwo.cities[0] = cromoTwo.cities[0]
    aux = cromoOne.cities[0]

    while aux != cromoTwo.cities[0]:
        for x in range(0,24):
            if cromoTwo.cities[x] == aux:
                sonTwo.cities[x] = aux
                aux = cromoOne.cities[x]


    for x in range(0,24):
        if sonTwo.cities[x] is None:
            sonTwo.cities[x] = cromoOne.cities[x]

    sonOne.setFitness(allCities)
    sonTwo.setFitness(allCities)

    arraySons.append(sonOne)
    arraySons.append(sonTwo)


def loadRoulette(arrayCromosomas):
    roulette = []

    for cromosoma in arrayCromosomas:
        for j in range(0, int(cromosoma.fitness * 10)):
            roulette.append(cromosoma.id)

    return roulette


def getCromosoma(id, cromosomas):
    for cromosoma in cromosomas:
        if cromosoma.id == id:
            return cromosoma


def mutation(cromosoma, allCities):
    posOneMut = random.randint(0,23)
    posTwoMut = random.randint(0,23)

    aux = cromosoma.cities[posOneMut]
    cromosoma.cities[posOneMut] = cromosoma.cities[posTwoMut]
    cromosoma.cities[posTwoMut] = aux

    cromosoma.setFitness(allCities)


if __name__ == '__main__':
    allCities = []
    cities = []
    fatherPoblation = []
    lenGenes = 23
    probMut = 0.05
    probCross = 0.75
    lenPoblation = 50
    file = 'TablaCapitales.xlsx'

    xl = pd.ExcelFile(file)

    df1 = xl.parse('Sheet1')

    cities.append(City(0, 'Cdad. de Bs. As.', df1['Cdad. de Bs. As.'], 222, 247))
    cities.append(City(1, 'Córdoba', df1['Córdoba'], 137, 183))
    cities.append(City(2, 'Corrientes', df1['Corrientes'], 224, 113))
    cities.append(City(3, 'Formosa', df1['Formosa'], 230, 87))
    cities.append(City(4, 'La Plata', df1['La Plata'], 225, 254))
    cities.append(City(5, 'La Rioja', df1['La Rioja'], 99, 159))
    cities.append(City(6, 'Mendoza', df1['Mendoza'], 69, 218))
    cities.append(City(7, 'Neuquén', df1['Neuquén'], 82, 331))
    cities.append(City(8, 'Paraná', df1['Paraná'], 196, 193))
    cities.append(City(9, 'Posadas', df1['Posadas'], 268, 115))
    cities.append(City(10, 'Rawson', df1['Rawson'], 129, 412))
    cities.append(City(11, 'Resistencia', df1['Resistencia'], 217, 109))
    cities.append(City(12, 'Río Galleqos', df1['Río Gallegos'], 94, 574))
    cities.append(City(13, 'S.F.d.V.d. Catamarca', df1['S.F.d.V.d. Catamarca'], 109, 133))
    cities.append(City(14, 'S.M. de Tucumán', df1['S.M. de Tucumán'], 118, 104))
    cities.append(City(15, 'S.S. de Jujuy', df1['S.S. de Jujuy'], 120, 54))
    cities.append(City(16, 'Salta', df1['Salta'], 116, 61))
    cities.append(City(17, 'San Juan', df1['San Juan'], 71, 194))
    cities.append(City(18, 'San Luis', df1['San Luis'], 107, 215))
    cities.append(City(19, 'Santa Fe', df1['Santa Fe'], 191, 189))
    cities.append(City(20, 'Santa Rosa', df1['Santa Rosa'], 138, 288))
    cities.append(City(21, 'Sgo. Del Estero', df1['Sgo. Del Estero'], 131, 117))
    cities.append(City(22, 'Ushuaia', df1['Ushuaia'], 114, 628))
    cities.append(City(23, 'Viedma', df1['Viedma'], 154, 366))

    allCities = cities.copy()

    print("--- Ingrese la opcion del menu ----")
    print("\ta) Ingresar una provincia y calcular el menor recorrido")
    print("\tb) Recorrido minimo para recorrer todas las ciudades")
    print("\tc) Utilizar algoritmo genetico\n")

    opt = input("¿Que desea hacer? ")

    if opt == "a":
        DistanceOfProvince(cities, allCities)
    elif opt == "b":
        MinimumDistance(allCities)
    elif opt == "c":
        initialPoblation = []

        for x in range(0, lenPoblation):
            oCromosoma = Cromosoma(x)

            while len(oCromosoma.cities) != 24:
                city = random.randint(0, 23)

                try:
                    oCromosoma.cities.index(city)
                except:
                    oCromosoma.cities.append(city)

            oCromosoma.setFitness(allCities)

            initialPoblation.append(oCromosoma)

        generations = 0
        generations = input('\n¿Cuantas generaciones quiere reproducir? ')
        for j in range(0, int(generations)):
            sonPoblation = []
            auxCreatePobllation = []

            # Roulette
            if not fatherPoblation:
                roulette = loadRoulette(initialPoblation)
                auxCreatePobllation = initialPoblation
            else:
                roulette = loadRoulette(fatherPoblation)
                auxCreatePobllation = fatherPoblation

            fatherPoblation = []
            # Create father poblation
            for x in range(0, lenPoblation):
                valRandom = random.randint(0, len(roulette) - 1)

                fatherPoblation.append(getCromosoma(roulette[valRandom], auxCreatePobllation))

            # Create son poblation
            for x in range(0, int(lenPoblation / 2)):
                if x != 0 :
                    if (x % 2 != 0):
                        x = x + 1

                fatherOne = fatherPoblation[x]
                fatherTwo = fatherPoblation[x + 1]

                isCrossover = random.uniform(0, 1)

                if isCrossover < probCross:
                    crossover(fatherOne, fatherTwo, sonPoblation, allCities)
                else:
                    sonPoblation.append(fatherOne)
                    sonPoblation.append(fatherTwo)

            for cromosoma in sonPoblation:
                isMutation = random.uniform(0, 1)

                if isMutation < probMut:
                    mutation(cromosoma, allCities)

            for x in range(0, len(sonPoblation)):
                sonPoblation[x].id = x + 1

            fatherPoblation = sonPoblation

        fatherPoblation.sort(key=lambda x: x.fitness, reverse=True)

        for cromo in fatherPoblation:
            print(10000 / cromo.fitness)

        bestCromosoma = fatherPoblation[0]

        visitedCities = []

        for city in bestCromosoma.cities:
            visitedCities.append(GetElement(allCities, city))

        root = Tk()
        canvas = Canvas(root, width = 373, height = 650)
        canvas.pack()
        img = PhotoImage(file="map.png")
        canvas.create_image(0, 0, anchor=NW, image=img)

        beforeCity = GetElement(allCities, bestCromosoma.cities[0])
        for city in visitedCities:
            canvas.create_line(beforeCity.x, beforeCity.y, city.x, city.y, width=2, fill="red")
            beforeCity = city

        mainloop()
