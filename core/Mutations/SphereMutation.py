import numpy as np
from abc import ABC, abstractmethod
from core import Population, Mutation
from core.Individual import Individual
import random
import math


class SphereMutation(Mutation):
    def __init__(self, probability: float, psm: float):
        """
        Constructor for the Sphere Mutation class.

        Parameters:
            probability (float): Probability of mutation (between 0 and 1).
            psm (float): The probability of mutating each individual in the population.
        """
        super().__init__(probability)
        self.psm = psm  # Probability of sphere mutation for each individual

    def _mutate(self, individual: Individual, population: Population) -> None:
        """
        Applies Sphere Mutation to the individual's chromosome.

        Parameters:
            individual (Individual): A single individual to mutate.
            population (Population): The population containing individuals.

        Returns:
            None: The population with mutated individuals.
        """
        self.sphere_mutation(individual.chromosome)

    def sphere_mutation(self, chromosome):
        if np.random.uniform(0, 1) <= self.psm:

            k, q = random.sample(range(len(chromosome)), 2)
            a = np.random.uniform(0, 1)
            B = math.sqrt((chromosome[k] / chromosome[q]) ** 2 * (1 - a ** 2) + 1)


            chromosome[k] = a * chromosome[k]
            chromosome[q] = B * chromosome[q]

        return None
