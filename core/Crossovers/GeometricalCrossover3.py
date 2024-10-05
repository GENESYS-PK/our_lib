import numpy as np
import math
import random

from core import Crossover, Population
from core.Individual import Individual
from core.Population import Population
from core.Representation import Representation


class GeometricalCrossover1(Crossover):
    """
    A class that implements Geometrical Crossover version 3 (Algorytmy genetyczne : kompendium. T. 1 strona 227)

    :param how_many_individuals: The number of individuals to create in the offspring.
    :param probability: The probability of performing the crossover operation.
    :param k: The number of individuals to draft from population for crossover needs
    :raises ValueError: If population size is less than 2 or k parameter is wrong.

    allowed_representation: [Representation.REAL]
    """

    allowed_representation = [Representation.REAL]

    def __init__(self, how_many_individuals: int, probability: float = 0, k: int = 2):
        super().__init__(how_many_individuals, probability)
        self.k = k

    def _cross(self, population_parent: Population) -> Population:
        """
        :param population_parent: The population to perform the crossover operation on.
        :param alfa: List of k random real numbers where each element belongs to <0,1> and all elements sum up to 1 used
        for blending two genes
        :returns: The offspring population (always 1 child).
        """

        if population_parent.population_size < 2:
            raise ValueError("The population size must be at least 2 to perform the GeometricalCrossover1 operation.")

        if self.k < 2 or self.k > population_parent.population_size:
            raise ValueError("The k parameter must be more than 2 and less than population_size")

        # drafting k individuals
        individuals_indices = [i for i in range(population_parent.population_size)]
        drafted_individuals = random.sample(individuals_indices, self.k)

        # creating alfa array
        floats = [random.random() for _ in range(len(drafted_individuals))]
        sum_floats = sum(floats)
        alfa = [x / sum_floats for x in floats]

        chromosome_size = len(population_parent.population[drafted_individuals[0]].chromosome)
        child_chromosome = np.zeros(chromosome_size)

        for i in range(chromosome_size):
            new_ind_val = 1
            for k in range(len(drafted_individuals)):
                new_ind_val *= math.pow(population_parent.population[drafted_individuals[k]].chromosome[i], alfa[k])
            child_chromosome[i] = new_ind_val

        child = Individual(chromosome=child_chromosome, value=0)

        return Population(population=[child])
