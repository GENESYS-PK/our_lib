import numpy as np
from abc import ABC, abstractmethod
from core import Population, Mutation
from core.Individual import Individual
import random


class BoundaryMutation(Mutation):
    """
    Implements boundary mutation where gene values are replaced by boundary values with a given probability.

    :param pbm: The probability of mutating each gene within an individual.
    :param boundaries: The allowed boundaries for each gene.
    """

    def __init__(self, probability: float, pbm: float, boundaries: list):
        super().__init__(probability)
        self.pbm = pbm  # Probability of boundary mutation for each gene
        self.boundaries = boundaries  # List of [min, max] boundaries for each gene

    def _mutate(self, individual: Individual, population: Population) -> None:
        """
        Perform boundary mutation on an individual.

        :param individual: The individual to mutate.
        :param population: The population containing the individual.
        :returns: None
        """
        individual.genome = self.boundary_mutation(individual.genome)

    def boundary_mutation(self, genome):
        """
        Apply boundary mutation on the genome of an individual.

        :param genome: List of gene values representing an individual's genome.
        :returns: Mutated genome.
        """
        for i in range(len(genome)):
            if np.random.uniform(0, 1) <= self.pbm:
                # Mutate gene to either lower or upper boundary
                if np.random.uniform(0, 1) < 0.5:
                    genome[i] = self.boundaries[i][0]
                else:
                    genome[i] = self.boundaries[i][1]
        return genome