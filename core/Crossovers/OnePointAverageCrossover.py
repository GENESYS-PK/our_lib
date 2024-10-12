import numpy as np
from core import Crossover, Population
from core.Individual import Individual
from core.Population import Population


class OnePointAverageCrossover(Crossover):
    def __init__(self, how_many_individuals: int, probability: float = 0):
        """
        Constructor for the OnePointAverageCrossover (1-PAX) class.

        :param how_many_individuals: The number of individuals to create in the offspring.
        :param probability: The probability of performing the crossover operation.
        """
        super().__init__(how_many_individuals, probability)

    def _cross(self, population_parent: Population) -> Population:
        """
        Perform one-point average crossover on the parent population.

        :param population_parent: The population to perform the crossover operation on.
        :returns: The offspring population.
        :raises ValueError: If the population size is less than 2.
        """
        if population_parent.population_size < 2:
            raise ValueError("The population size must be at least 2 "
                             "to perform the OnePointAverageCrossover operation.")

        offspring_population = Population()

        # Randomly select two parents from the parent population
        parent_indices = np.random.choice(population_parent.population_size, 2, replace=False)
        parent_x = population_parent.population[parent_indices[0]].chromosome
        parent_y = population_parent.population[parent_indices[1]].chromosome

        # Crossover point - select a point for crossover
        size = min(len(parent_x), len(parent_y))
        crossover_point = np.random.randint(0, size)

        # Create new individuals where only one point is averaged
        new_ind_x = np.copy(parent_x)
        new_ind_y = np.copy(parent_y)

        # Averaging at the crossover point
        new_ind_x[crossover_point] = (parent_x[crossover_point] + parent_y[crossover_point]) / 2
        new_ind_y[crossover_point] = (parent_x[crossover_point] + parent_y[crossover_point]) / 2

        # Add new individuals to the offspring population
        offspring_population.add_to_population(Individual(new_ind_x))
        offspring_population.add_to_population(Individual(new_ind_y))

        return offspring_population
