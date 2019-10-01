#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

# hay que cambiar la funcion objetivo a un calculo de mejor ruta
class Chromosome(object):

    # Constructor / Instance Attributes
    def __init__(self, large, cities, newRoute):
        # Chromosome's Genes
        if newRoute is None:
            for _ in range(large):
                self.route = random.shuffle(cities)
        else:
            self.route = newRoute
        self.large = large
        # Initialize Objective Function Punctuation and Fitness
        self.setObjectivePunctuation()
        self.fitness = 0

    # Show All Genes of the Chromosome
    def getRoute(self):
        return self.route

        return int(str_bin_num)

    def calcObjPunc(self):
        pass

    def calcFitness(self, totalObj):
        # if totalObj == 0: totalObj = 1  # Prevent Division by Zero Error
        self.fitness = (self.getObjectivePunctuation() / totalObj)  # Update Fitness
        return self.fitness

    # Getters and Setters
    def getLarge(self):
        return self.large

    def setLarge(self, large):
        self.large = large

    def getObjectivePunctuation(self):
        return self.objectivePunctuation

    def setObjectivePunctuation(self):
        self.objectivePunctuation = self.calcObjPunc()

    def getFitness(self):
        return self.fitness

    def setFintess(self, fitness):
        self.fitness = fitness
