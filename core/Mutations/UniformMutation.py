import numpy as np
from population import Population
from mutation import Mutation
from core.Individual import Individual
import random

class UniformMutation(Mutation):
    """
    The class implements Uniform mutation, where a random gene in the chromosome is selected,
    and its value is replaced with another random value from the domain.

    :param probability: The probability of performing the mutation operation.
    :param domain: The domain of gene
    :param allowed_representation: A list of allowed representations for the mutation operation.
    """
    allowed_representation = []

    def __init__(self, domain:list[float], probability: float = 0):
        super().__init__(probability)
        self.domain = domain

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
        new_value_of_gene = random.uniform(self.domain[0], self.domain[1])
        individual.chromosome[mutation_point] = new_value_of_gene