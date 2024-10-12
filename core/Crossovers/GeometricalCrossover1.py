import numpy as np
import math
import random

from core import Crossover, Population
from core.Individual import Individual
from core.Population import Population
from core.Representation import Representation


class GeometricalCrossover1(Crossover):
    """
    A class that implements Geometrical Crossover version 1 (Algorytmy genetyczne: kompendium. T. 1 strona 227)

    :param how_many_individuals: The number of individuals to create in the offspring.
    :param probability: The probability of performing the crossover operation.
    :raises ValueError: If population size is less than 2.

    allowed_representation: [Representation.REAL]
    """

    allowed_representation = [Representation.REAL]

    def __init__(self, how_many_individuals: int, probability: float = 0):
        super().__init__(how_many_individuals, probability)

    def _cross(self, population_parent: Population) -> Population:
        """
        :param population_parent: The population to perform the crossover operation on.
        :returns: The offspring population (always 1 child).
        """

        individual_index1 = np.random.randint(population_parent.population_size)
        individual_index2 = np.random.randint(population_parent.population_size)

        while individual_index1 == individual_index2:
            individual_index2 = np.random.randint(population_parent.population_size)

        # not sure if this approach is right
        chance_crossover = np.round(np.random.uniform(0, 1), 2)
        if self.probability < chance_crossover <= 1:
            return Population()

        chromosome_size = len(population_parent.population[individual_index1].chromosome)
        child_chromosome = np.zeros(chromosome_size)
        for i in range(chromosome_size):
            child_chromosome[i] = math.sqrt(population_parent.population[individual_index1].chromosome[i] *
                                            population_parent.population[individual_index2].chromosome[i])

        child = Individual(chromosome=child_chromosome, value=0)

        return Population(population=[child])
