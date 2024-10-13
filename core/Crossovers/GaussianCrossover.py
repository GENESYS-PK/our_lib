import numpy as np
import random
import math
from core import Crossover, Individual, Population


class GaussCrossover(Crossover):
    """
    Implements Gauss crossover method based on the Gaussian mechanism.

    :param how_many_individuals: The number of individuals to create in the offspring.
    :param fitness_function: A callable fitness function that evaluates individuals.
    :param xp: The lower bound for offspring values.
    :param xk: The upper bound for offspring values.
    :param probability: The probability of performing the crossover operation.
    """

    allowed_representation = []

    def __init__(self, how_many_individuals: int, fitness_function: callable, xp: float, xk: float,
                 probability: float = 0):
        super().__init__(how_many_individuals, probability)
        self.fitness_function = fitness_function
        self.xp = xp
        self.xk = xk

    def cross(self, population_parent: Population) -> Population:
        """
        Perform the crossover operations for the entire population.

        :param population_parent: The population to perform the crossover operation on.
        :returns: The offspring population.
        """
        offspring = Population()

        while offspring.population_size < population_parent.population_size:
            if np.random.rand() < self.probability:
                offspring.add_to_population(self._cross(population_parent))

        offspring.trim_children(self.how_many_individuals)
        return offspring

    def _cross(self, population_parent: Population) -> Population:
        """
        Perform Gaussian crossover between two individuals from the parent population.

        :param population_parent: The population to perform the crossover operation on.
        :returns: A list containing the offspring.
        """
        parent_1, parent_2 = population_parent.select_two()

        size = min(len(parent_1), len(parent_2))
        offspring1 = []
        offspring2 = []

        for i in range(size):
            distance = math.fabs(parent_1[i] - parent_2[i])
            alpha = random.random()

            if random.uniform(0, 1) <= 0.5:
                new_val1 = parent_1[i] + alpha * (distance / 3)
                new_val2 = parent_2[i] + alpha * (distance / 3)
            else:
                new_val1 = parent_2[i] + alpha * (distance / 3)
                new_val2 = parent_1[i] + alpha * (distance / 3)

            # Check bounds
            if new_val1 < self.xp or new_val1 > self.xk:
                new_val1 = parent_1[i]
            if new_val2 < self.xp or new_val2 > self.xk:
                new_val2 = parent_2[i]

            offspring1.append(new_val1)
            offspring2.append(new_val2)


        offspring = []
        offspring.append(offspring1)
        offspring.append(offspring2)

        return offspring
