import numpy as np
from core import Mutation, Individual, Population

class BreederGAMutation(Mutation):
    def __init__(self, probability: float, k: float, ranges: list):
        """
        Constructor for the BreederGAMutation class.

        Parameters:
            probability (float): Probability of mutation (between 0 and 1).
            k (float): Mutation precision parameter.
            ranges (list): List of mutation ranges for each gene.
        """
        super().__init__(probability)
        self.k = k
        self.ranges = ranges

    def _mutate(self, individual: Individual, population: Population) -> None:
        """
        Applies Breeder GA mutation to the individual's chromosome.

        Parameters:
            individual (Individual): A single individual to mutate.
            population (Population): The population containing individuals.

        Returns:
            None: The population with mutated individuals.
        """
        chromosome = individual.chromosome

        for i in range(len(chromosome)):
            if np.random.uniform(0, 1) <= self.probability:
                alfa = np.random.uniform(0, 1)

                if np.random.uniform(0, 1) <= 0.5:
                    chromosome[i] -= self.ranges[i] * 2 ** (-self.k * alfa)
                else:
                    chromosome[i] += self.ranges[i] * 2 ** (-self.k * alfa)

        individual.chromosome = chromosome
