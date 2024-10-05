import numpy as np
from abc import ABC, abstractmethod
from core import Population, Mutation
from core.Individual import Individual
import random
import math


class SphereMutation(Mutation):
    """
    Implements sphere mutation where gene values are adjusted based on random selection of two genes.

    :param psm: The probability of mutating each individual in the population.
    """

    def __init__(self, probability: float, psm: float):
        super().__init__(probability)
        self.psm = psm  # Probability of sphere mutation for each individual

    def _mutate(self, individual: Individual, population: Population) -> None:
        """
        Perform sphere mutation on an individual.

        :param individual: The individual to mutate.
        :param population: The population containing the individual.
        :returns: None
        """
        self.sphere_mutation(individual.chromosome)

    def sphere_mutation(self, chromosome):
        """
        Apply sphere mutation on the chromosome of an individual.

        :param chromosome: List of gene values representing an individual's chromosome.
        :returns: None
        """
        if np.random.uniform(0, 1) <= self.psm:
            # Randomly select two genes to mutate
            k, q = random.sample(range(len(chromosome)), 2)
            a = np.random.uniform(0, 1)
            B = math.sqrt((chromosome[k] / chromosome[q]) ** 2 * (1 - a ** 2) + 1)

            # Apply the mutation
            chromosome[k] = a * chromosome[k]
            chromosome[q] = B * chromosome[q]

        return None
