#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


class Chromosome(object):

    # Class Attribute
    CitiesDict = {}

    # Constructor / Instance Attributes
    def __init__(self, large, cities, newRoute):
        # Chromosome's Genes
        if newRoute is None:
            random.shuffle(cities)
            self.route = []
            for i in range(len(cities)):
                self.route.append(cities[i])  # Shuffle and then Assignation
            print(self.route)
        else:
            self.route = newRoute
        self.large = large
        self.objectivePunctuation = 0
        self.fitness = 0

        # Initialize Objective Function Punctuation
        self.setObjectivePunctuation()


    @classmethod
    def getCitiesDict(cls):
        return cls.CitiesDict

    @classmethod
    def setCitiesDict(cls, citiesDictionary):
        cls.CitiesDict = citiesDictionary

    # Show All Genes of the Chromosome
    def getRoute(self):
        return self.route

    def calcObjPunc(self):
        accumulated_distance = 0
        cd = self.getCitiesDict()
        city_last = self.route[0]
        # Calculate Distance Step by Step comparing the Chromosome's Route with Neighbours on Cities Dictionary
        for i in range(1, len(self.route)-2):
            city_step = self.route[i]
            accumulated_distance += cd[city_last].get_distance_to(cd[city_step])
            city_last = city_step
        # At the End, go back to the First City
        accumulated_distance += cd[self.route[len(self.route)-1]].get_distance_to(cd[self.route[0]])
        return accumulated_distance

    def calcFitness(self, totalObj):  # Reverse Score (Little Distances gets better Fitness)
        # self.fitness = 1000 / self.getObjectivePunctuation()
        self.fitness = totalObj / (totalObj - self.getObjectivePunctuation()) - 1  # Update Fitness
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

    """
    def copy(self, another_crom, start, end):
        for i in range(start, end):
            self.route[i] = (another_crom.route[i])
    """