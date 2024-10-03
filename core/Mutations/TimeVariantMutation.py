import numpy as np
from abc import ABC, abstractmethod
from core import Population, Mutation
from core.Individual import Individual
import random
import math


class TimeVariantMutation(Mutation):
    """
    Implements time-variant mutation where the mutation scale reduces over time.

    :param ypsilon: A constant that controls the strength of the mutation.
    :param t: Current generation.
    :param M: Maximum number of generations.
    :param k: The index of the gene to mutate.
    """

    def __init__(self, probability: float, ypsilon: float, t: int, M: int, k: int):
        super().__init__(probability)
        self.ypsilon = ypsilon  # Controls mutation strength
        self.t = t  # Current generation
        self.M = M  # Maximum generations
        self.k = k  # Index of gene to mutate

    def _mutate(self, individual: Individual, population: Population) -> None:
        """
        Perform time-variant mutation on an individual.

        :param individual: The individual to mutate.
        :param population: The population containing the individual.
        :returns: None
        """
        individual.genome = self.time_variant_mutation(individual.genome)

    def time_variant_mutation(self, genome):
        """
        Apply time-variant mutation on the genome of an individual.

        :param genome: List of gene values representing an individual's genome.
        :returns: Mutated genome.
        """
        for j in range(len(genome)):
            r = np.random.uniform(0, 1)
            sigma = 1 - (r ** (1 - self.t / self.M)) ** self.ypsilon
            a = np.random.normal(0, sigma ** 2)
            genome[self.k] = genome[self.k] + a
        return genome