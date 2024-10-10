import numpy as np
from population import Population
from mutation import Mutation
from core.Individual import Individual
import random

class ModifiedUniformMutation(Mutation):
    """
  The class implements modified uniform mutation, where a random gene in the chromosome is selected,
    and its value is replaced with another value from the surrounding of actual value. The
    size of this surrounding is related to scaling K parameter. Initially value of this parameter is
    big and decreasing with the progress of algorithm iterations. This allows the search to be global
    in the initial phases of the algorithm's execution, while becoming local in the final phases.

:param probability: The probability of performing the mutation operation.
    :param domain: The domain of gene
    :param current_iteration: The current iteration number of algorithm
    :param max_number_of_iteration: The maximum number of iterations
    :param allowed_representation: A list of allowed representations for the mutation operation.
    """
    allowed_representation = []

    def __init__(self, domain: list[float], current_iteration: int, max_number_of_iteration: int, probability: float = 0):
        super().__init__(probability)
        self.domain = domain
        self.current_iteration = current_iteration
        self.max_number_of_iteration = max_number_of_iteration

    def mutate(self, population_parent: Population) -> Population:
        """
        Perform the mutation operations for the entire population.

        :param population_parent: The population to perform the mutation operation on.
        :returns: The mutated population.
        """
        for individual in population_parent.population:
            if np.random.rand() < self.probability:
                self._mutate(individual, population_parent)

        return population_parent

    def _mutate(self, individual: Individual, population: Population) -> None:
        """
        :param individual: The individual to perform the mutation operation on.
        :param population: The population to which the individual belongs.
        :returns: None
        """
        mutation_point = random.randint(0, len(individual.chromosome) - 1)
        alfa = random.randint(1, 10)
        delta = (self.domain[1] - self.domain[0]) / alfa

        random_number = random.uniform(0, 1)
        k_parameter = 1 - (self.current_iteration * (1/self.max_number_of_iteration))
        if random_number <= 0.5:
            individual.chromosome[mutation_point] = individual.chromosome[mutation_point] + (k_parameter * delta)
        else:
            individual.chromosome[mutation_point] = individual.chromosome[mutation_point] - (k_parameter * delta)