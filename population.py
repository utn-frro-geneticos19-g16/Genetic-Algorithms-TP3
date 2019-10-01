#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chromosome import Chromosome
import random

# HAY QUE CAMBIAR LA RULETA, LA FUNCION OBJETIVO, Y EL CROSSOVER A CICLICO!!!
class Population(object):
    # Class Attributes
    population = []  # Initial Population (Array of Chromosomes)
    totalObjPunc = 0  # The Sum of All Objective Functions Punctuation
    totalFitness = 0  # The Sum of All Objective Values

    bestTrack = None
    cantKM = 1000000

    # Constructor / Instance Attributes
    def __init__(self, numChroms, cities, crossProb, mutProb):
        self.numChroms = numChroms
        self.chromSize = len(cities)
        self.crossProb = crossProb
        self.mutProb = mutProb

        print("Start Algorithm")
        for _ in range(numChroms):
            oneChrom = Chromosome(chromSize, cities, None)  # Initialization of Chromosomes
            self.addChrom(oneChrom)  # Add to Population

    # Show Actual Population and Stats
    def showPopulation(self, numIter):
        self.setTotalFitness(0)
        self.setTotalObjPunc(self.calcTotalObjPunc())
        large = self.getChromSize()
        averageObjPunc = self.getTotalObjPunc() / len(self.population)
        fitness = 0
        maxVal = 0
        minVal = 0
        maxChrom = 0
        minChrom = 0
        print("Population ", (numIter + 1), ":")
        for i in range(len((self.population))):
            fitness = self.population[i].calcFitness(self.getTotalObjPunc())
            self.updateTotalFitness(fitness)
            if i == 0:
                maxVal = fitness
                minVal = fitness
            elif fitness > maxVal:
                maxVal = fitness
                maxChrom = i
            elif fitness < minVal:
                minVal = fitness
                minChrom = i
            for j in range(large):
                print(self.population[i].getBody()[j], '\n')
            print()
        fitness = self.getTotalFitnessAverage()
        print()
        print("Chromosome --- Value --- Objective Punctuation --- Fitness")
        print("Max Values: Chrom Nº", maxChrom, "with:", self.population[maxChrom].getRealValue(), "Val,",
              self.population[maxChrom].getObjectivePunctuation(), "OP,", round(maxVal, 4), "Fit")
        print("Min Values: Chrom Nº", minChrom, "with:", self.population[minChrom].getRealValue(), "Val,",
              self.population[minChrom].getObjectivePunctuation(), "OP,", round(minVal, 4), "Fit")
        print("Average OP:", averageObjPunc, "--- Average Fitness:", fitness)  # round(fitness,6)
        print()

    def getBestTrackAg(self):
        return bestTrack, cantKM

    # Calculate Total of Objective Functions Punctuation in the actual Generation
    def calcTotalObjPunc(self):
        acumObjPunc = 0
        for chromosome in self.population:
            acumObjPunc += chromosome.getObjectivePunctuation()  # Add Every Objective Function Punctuation
        return acumObjPunc

    # Update Total Fitness
    @classmethod
    def updateTotalFitness(cls, fitness):
        cls.totalFitness += fitness

    # Add to Population
    def addChrom(self, Chrom):
        self.population.append(Chrom)

    # Reproduction
    def reproduce(self):
        parents = []  # List of Potential Parents
        newGeneration = []  # List of Children
        print("Roulette Results: ", '\n')
        #  lastParent = None  # Check if a Chromosome tries to reproduce with himself
        for _ in range(0, len(self.population), 2):
            lastParent = None
            for i in range(2):
                lastParent = self.roulette(lastParent)  # Parents Selected by Roulette
                parents.append(self.population[lastParent])
        print()
        for i in range(0, len(parents), 2):
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
                son1 = self.mutation(son1)
            if self.mutationPosibility():
                son2 = self.mutation(son2)
            self.addChildren(son1, son2, newGeneration)
        self.replacePopulation(newGeneration)
        self.setTotalFitness(0)

    # Genetic Operator (Roulette Method)
    def roulette(self, lastParent):
        # Generator of a Bidimensional List (Fitness Range of Chromosomes)
        newRoulette = [[0] * 2 for _ in range(len(self.population))]
        acum = 0  # Acumulator of Relative Fitness from 0 to 1 (Fills Roulette)
        for i in range(len(self.population)):
            newRoulette[i][0] = acum  # Range Min: Last Acum Value
            acum += round(self.population[i].getFitness(), 6)  # Acum's Value From Zero
            newRoulette[i][1] = acum  # Range Max: New Acum Value
        ranNum = round(random.uniform(0, 1), 6)  # Random Number from 0.000000 to 0.999999
        # print("Random: ", ranNum)  # Only Print
        count = 0
        while count <= 100:  # If the same parent is selected more than 100 times... select the next or last one
            for i in range(len(newRoulette)):
                if newRoulette[i][0] < ranNum < newRoulette[i][1]:
                    # Return Selected Chromosome if the Random Number Exists in its Range
                    if lastParent != i:
                        print(i, ', ')
                        return i
                    else:
                        print("REP", ', ')
                        ranNum = round(random.uniform(0, 1), 6)
                        break
            count += 1
            if count == 100:  # Reach Only if the same parent goes selected 100 times
                if lastParent < len(newRoulette)-1:
                    print(lastParent, ', ')
                    return lastParent+1
                else:
                    print(lastParent, ', ')
                    return lastParent-1
        print("Error")
        return "Error"  # Error Exit

    def crossPosibility(self):  # CrossOver posibility evaluation
        if self.getCrossProb()*100 >= random.randint(1, 100):
            return True
        else:
            return False

    def cross(self, parent1, parent2):
        crom_size = parent1.getLarge()
        son1 = Chromosome(crom_size, None)
        son2 = Chromosome(crom_size, None)
        cut = random.randint(1, crom_size - 2)  # Random Cut Point (Except by zero or all genes)

        son1.copy(parent1, 0, cut)
        son1.copy(parent2, cut, crom_size)

        son2.copy(parent2, 0, cut)
        son2.copy(parent1, cut, crom_size)

        son1.setObjectivePunctuation()
        son2.setObjectivePunctuation()

        print()
        print("Son 1:", son1.toBinInteger())  # Only Print
        print("Son 2:", son2.toBinInteger())  # Only Print
        print("Cut Point on:", cut)  # Only Print
        return son1, son2

    def copy(self, chrom1, chrom2):
        # newGeneration.append(chrom1)
        # newGeneration.append(chrom2)
        son1 = chrom1
        son2 = chrom2
        print()
        print("Son 1 (Identical):", self.listToInt(chrom1.getBody()))  # Only Print
        print("Son 2 (Identical):", self.listToInt(chrom2.getBody()))  # Only Print
        return son1, son2

    def mutationPosibility(self):  # Mutation posibility evaluation
        if self.getMutProb() * 100 >= random.randint(1, 100):
            return True
        else:
            return False

    def mutation(self, chrom):  # Select one random Gen and Switch its Value
        mutPos = random.randint(1, self.chromSize)
        newBody = []
        for i in range(len(chrom.getBody())):
            if i != mutPos:
                newBody.append(chrom.getBody()[i])
            else:
                if chrom.getBody()[mutPos] == 1:  # If is a '0' then change to '1', and vice-versa
                    newBody.append(0)
                else:
                    newBody.append(1)
        son = Chromosome(self.chromSize, newBody)
        print("Mutated Chrom in position:", mutPos, ":", self.listToInt(chrom.getBody()))  # Only Print
        return son

    def addChildren(self, son1, son2, newGeneration):
        newGeneration.append(son1)
        newGeneration.append(son2)

    def replacePopulation(self, newGeneration):  # Replace All Population in every Iteration
        self.population = []
        for i in range(len(newGeneration)):
            self.population.append(newGeneration[i])

    def listToInt(self, arr):
        num = ''.join(str(i) for i in arr)
        return int(num)

    # Class Getters and Setters
    @classmethod
    def getTotalObjPunc(cls):
        return cls.totalObjPunc

    @classmethod
    def setTotalObjPunc(cls, total):
        cls.totalObjPunc = total

    @classmethod
    def getTotalFitness(cls):
        return cls.totalFitness

    @classmethod
    def setTotalFitness(cls, total):
        cls.totalFitness = total

    @classmethod
    def getTotalFitnessAverage(cls):
        return cls.totalFitness / len(cls.population)

    # Getters and Setters 
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
