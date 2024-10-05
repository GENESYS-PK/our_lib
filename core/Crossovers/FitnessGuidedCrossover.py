import numpy as np
import random
from core import Crossover, Population


class FitnessGuidedCrossover(Crossover):
    """
    Implements fitness-guided crossover method based on the fitness values of the parents.

    :param how_many_individuals: The number of individuals to create in the offspring.
    :param probability: The probability of performing the crossover operation.
    :param fitness_function: A callable fitness function that evaluates individuals.
    :param beta: Defines the range for alpha (-beta ≤ alpha ≤ beta).
    """

    allowed_representation = []

    def __init__(self, how_many_individuals: int, fitness_function: callable, probability: float = 0,
                 beta: float = 0.5):
        super().__init__(how_many_individuals, probability)
        self.fitness_function = fitness_function
        self.beta = beta

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
        Perform fitness-guided crossover on two parents from the population.

        Parameters:
            population_parent (Population): The parent population.

        Returns:
            Population: A population containing offspring individuals created by crossover.
        """
        while True:
            parent_1, parent_2 = random.sample(population_parent.population, 2)
            if parent_1 != parent_2:
                break

        p1_chromosome = parent_1.chromosome
        p2_chromosome = parent_2.chromosome

        alpha = np.random.uniform(-self.beta, self.beta)

        if self.fitness_function(*p1_chromosome) < self.fitness_function(*p2_chromosome):
            child = [p1_chromosome[i] + alpha * (p1_chromosome[i] - p2_chromosome[i]) for i in range(len(p1_chromosome))]
        else:
            child = [p2_chromosome[i] + alpha * (p2_chromosome[i] - p1_chromosome[i]) for i in range(len(p1_chromosome))]

        offspring = child
        return offspring

