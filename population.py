#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chromosome import Chromosome
import random


class Population(object):
    # Constructor / Instance Attributes
    def __init__(self, numChroms, cities, crossProb, mutProb):
        self.population = []  # Initial Population (Array of Chromosomes)
        self.totalObjPunc = 0  # The Sum of All Objective Functions Punctuation
        self.totalFitness = 0  # The Sum of All Objective Values
        self.numChroms = numChroms
        self.chromSize = len(cities)
        self.crossProb = crossProb
        self.mutProb = mutProb
        self.bestTrack = None
        self.bestTrackDistance = 1000000

        print("Start Algorithm")
        for i in range(numChroms):
            print("Chrom ", i, end=": ")
            # Initialization of Chromosomes
            self.population.append(Chromosome(self.chromSize, cities, None))  # Add to Population

    # Show Actual Population and Stats
    def showPopulation(self, numIter):
        self.setTotalFitness(0)
        self.setTotalObjPunc(self.calcTotalObjPunc())
        large = self.getChromSize()
        averageObjPunc = self.getTotalObjPunc() / len(self.population)
        fitness = 0
        maxVal = 0
        secondMaxVal = 0
        minVal = 0
        bestRoutePos = 0
        secondBestRoutePos = 0
        worstRoutePos = 0
        print()
        print()
        print("Population ", (numIter + 1), ":")
        for i in range(len(self.population)):
            fitness = self.population[i].calcFitness(self.getTotalObjPunc())
            self.updateTotalFitness(fitness)
            if i == 0:
                maxVal = fitness
                minVal = fitness
            elif fitness > maxVal:
                maxVal = fitness
                bestRoutePos = i
            elif fitness < minVal:
                minVal = fitness
                worstRoutePos = i
            elif (fitness > secondMaxVal) and (fitness < maxVal):
                secondMaxVal = fitness
                secondBestRoutePos = i
            # for j in range(large):
                # print(self.population[i].getRoute()[j], end=', ')
            print(self.population[i].getRoute())
        fitness = self.getTotalFitnessAverage()

        # Setting Current Generation's Best Values (If Improves Actual Best)
        if self.population[bestRoutePos].getAccumulatedDistance() < self.getBestTrackDistance():
            self.setBestTrack(self.population[bestRoutePos])
            self.setBestTrackDistance(self.population[bestRoutePos].getAccumulatedDistance())

        print()
        print("Generation", numIter+1, "Final Status:")
        print("Worst Value: Route Nº", worstRoutePos, "with:",
              self.population[worstRoutePos].getObjectivePunctuation(), "OP,", round(minVal, 4), "Fit")
        print("Best Value: Route Nº", bestRoutePos, "with:",
              self.population[bestRoutePos].getObjectivePunctuation(), "OP,", round(maxVal, 4), "Fit")
        print("Total Distance of Best Route:", self.getBestTrackDistance(), "km")
        print("Average OP:", averageObjPunc, "--- Average Fitness:", round(self.getTotalFitnessAverage(), 6))
        print("---")
        print()

        elitChrom = self.population[bestRoutePos]
        secondElitChrom = self.population[secondBestRoutePos]

        return {
            "AverageOP": averageObjPunc,
            "MinOP": self.population[worstRoutePos].getObjectivePunctuation(),
            "MaxOP": self.population[bestRoutePos].getObjectivePunctuation(),
            "ElitChrom": elitChrom,
            "SecondElitChrom": secondElitChrom
        }

    # Get the Best Values
    def getBestTrackAg(self):
        return self.getBestTrack(), self.getBestTrackDistance()

    # Calculate Total of Objective Functions Punctuation in the actual Generation
    def calcTotalObjPunc(self):
        acumObjPunc = 0
        for chromosome in self.population:
            acumObjPunc += chromosome.getObjectivePunctuation()  # Add Every Objective Function Punctuation
        return acumObjPunc

    # Update Total Fitness
    def updateTotalFitness(self, fitness):
        self.totalFitness += fitness

    def getBestTrack(self):
        return self.bestTrack

    def setBestTrack(self, track):
        self.bestTrack = track

    def getBestTrackDistance(self):
        return self.bestTrackDistance

    def setBestTrackDistance(self, trackDistance):
        self.bestTrackDistance = trackDistance

    # Add to Population
    def addChrom(self, Chrom):
        self.population.append(Chrom)

    # Reproduction
    def reproduce(self, elitChrom, secondElitChrom):
        parents = []  # List of Potential Parents
        newGeneration = []  # List of Children

        # Elitism
        parents.append(elitChrom)
        parents.append(secondElitChrom)

        print("Roulette Results: ", end='')
        for _ in range(len(self.population)):
            indexSelectedParent = self.roulette()  # Parents Selected by Roulette
            if indexSelectedParent is not None:
                parents.append(self.population[indexSelectedParent])
            else:
                parents.append(self.population[0])  # Elite Chromosome
                print(0, end=', ')
        print()
        for i in range(2, len(parents), 2):
            father1 = parents[i]
            father2 = parents[i + 1]
            if self.crossPosibility():  # CrossOver Probability Evaluation
                son1, son2 = self.cross(father1, father2)  # CrossOver
                print("Successful CrossOver in reproduction:", (i + 2) / 2)  # Only Print
            else:
                son1, son2 = self.copy(father1, father2)  # Direct Assignation (Without CrossOver)
                print("CrossOver didn't happen in reproduction:", (i + 2) / 2)  # Only Print
            # Individual Mutation Probability Evaluation
            if self.mutationPosibility():
                son1.mutate()
            if self.mutationPosibility():
                son2.mutate()

            son1.setObjectivePunctuation()
            son2.setObjectivePunctuation()

            self.addChildren(son1, son2, newGeneration)
        self.replacePopulation(newGeneration)
        self.setTotalFitness(0)

    # Genetic Operator (Roulette Method)
    def roulette(self):
        # Generator of a Bidimensional List (Fitness Range of Chromosomes)
        newRoulette = [[0] * 2 for _ in range(len(self.population))]
        acum = 0  # Acumulator of Relative Fitness from 0 to 1 (Fills Roulette)
        for i in range(len(self.population)):
            newRoulette[i][0] = acum  # Range Min: Last Acum Value
            acum += self.population[i].getFitness()  # Acum's Value From Zero
            newRoulette[i][1] = acum  # Range Max: New Acum Value
        ranNum = random.uniform(0, 1)  # Random Number from 0.000000 to 0.999999
        for i in range(len(newRoulette)):
            if newRoulette[i][0] <= ranNum <= newRoulette[i][1]:
                # Return Selected Chromosome if the Random Number Exists in its Range
                print(i, end=', ')
                return i
        return None  # Error Return

    def crossPosibility(self):  # CrossOver posibility evaluation
        if self.getCrossProb()*100 >= random.randint(1, 100):
            return True
        else:
            return False

    # Cyclic Crossover
    def cross(self, parent1, parent2):
        crom_size = parent1.getLarge()

        newRoute1 = ['']*crom_size
        newRoute2 = ['']*crom_size

        newRoute1[0] = parent1.route[0]
        aux = parent2.route[0]
        pos = None
        while aux != parent1.route[0]:
            for i in range(crom_size):
                if parent1.route[i] == aux:
                    pos = i
                    break
            newRoute1[pos] = aux
            aux = parent2.route[pos]

        for i in range(crom_size):
            if newRoute1[i] == '':
                newRoute1[i] = parent2.route[i]

        newRoute2[0] = parent2.route[0]
        aux = parent1.route[0]
        pos = None
        while aux != parent2.route[0]:
            for i in range(crom_size):
                if parent2.route[i] == aux:
                    pos = i
                    break
            newRoute2[pos] = aux
            aux = parent1.route[pos]

        for i in range(crom_size):
            if newRoute2[i] == '':
                newRoute2[i] = parent1.route[i]

        son1 = Chromosome(crom_size, None, newRoute1)
        son2 = Chromosome(crom_size, None, newRoute2)

        print()
        print("New Sons after CrossOver: ")
        print(son1.getRoute())
        print(son2.getRoute())

        return son1, son2

    def copy(self, chrom1, chrom2):
        crom_size = chrom1.getLarge()
        newRoute1 = chrom1.getRoute()
        newRoute2 = chrom2.getRoute()
        son1 = Chromosome(crom_size, None, newRoute1)
        son2 = Chromosome(crom_size, None, newRoute2)

        print()
        print("New Sons without CrossOver (Indentical): ")
        print(son1.getRoute())
        print(son2.getRoute())

        return son1, son2

    def mutationPosibility(self):  # Mutation posibility evaluation
        if self.getMutProb() * 100 >= random.randint(1, 100):
            return True
        else:
            return False

    def addChildren(self, son1, son2, newGeneration):
        newGeneration.append(son1)
        newGeneration.append(son2)

    def replacePopulation(self, newGeneration):  # Replace All Population in every Iteration
        self.population = []
        for i in range(len(newGeneration)):
            self.population.append(newGeneration[i])

    def getTotalObjPunc(self):
        return self.totalObjPunc

    def setTotalObjPunc(self, total):
        self.totalObjPunc = total

    def getTotalFitness(self):
        return self.totalFitness

    def setTotalFitness(self, total):
        self.totalFitness = total

    def getTotalFitnessAverage(self):
        return self.totalFitness / len(self.population)

    def getNumChroms(self):
        return self.numChroms

    def setNumChroms(self, numChroms):
        self.numChroms = numChroms

    def getChromSize(self):
        return self.chromSize

    def setChromSize(self, chromSize):
        self.chromSize = chromSize

    def getCrossProb(self):
        return self.crossProb

    def setCrossProb(self, crossProb):
        self.crossProb = crossProb

    def getMutProb(self):
        return self.mutProb

    def setMutProb(self, mutProb):
        self.mutProb = mutProb
