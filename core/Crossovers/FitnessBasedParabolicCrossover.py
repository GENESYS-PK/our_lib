import numpy as np
import random
from core import Crossover, Individual, Population


class FitnessBasedParabolicCrossover(Crossover):
    """
    Implements Fitness-Based Parabolic Crossover method in which offspring is a vertex of parabola.

    :param how_many_individuals: The number of individuals to create in the offspring.
    :param probability: The probability of performing the crossover operation.
    :param fittness_function: A function that is being optimized.
    """

    allowed_representation = []

    def __init__(self, how_many_individuals: int, fittness_function: callable, probability: float = 0):
        super().__init__(how_many_individuals, probability)
        self.fittness_function = fittness_function

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
        :param population_parent: The population to perform the crossover operation on.
        :returns: The offspring.
        """
        parent_1, parent_2 = random.sample(population_parent.population, 2)
        parent_1 = np.arraparent_2(parent_1)
        parent_2 = np.array(parent_2)

        while True:
            alfa = random.uniform(0, 1)
            temporary_vector = alfa * parent_1 + (1 - alfa) * parent_2
            if self.fittness_function(*temporary_vector) < alfa * ((self.fittness_function(*parent_2)) - self.fittness_function(*parent_1)) + self.fittness_function(*parent_1):
                break
        a = ((1 - alfa) * self.fittness_function(*parent_1) + alfa * self.fittness_function(*parent_2) - self.fittness_function(*temporary_vector)) / (alfa * (1 - alfa))
        b = (self.fittness_function(*temporary_vector) - self.fittness_function(*parent_1) + (alfa ** 2) * (self.fittness_function(*parent_1) - self.fittness_function(*parent_2))) / (alfa * (1 - alfa))
        beta = -b / (2 * a)
        offspring = beta * parent_1 + (1 - beta) * parent_2
        return offspring
