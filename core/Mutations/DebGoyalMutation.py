import numpy as np
from core import Mutation, Individual, Population


class DebGoyalMutation(Mutation):
    def __init__(self, probability: float, n: int, delta_max: float):
        """
        Constructor of the DebGoyalMutation class.

        Parameters:
            probability (float): Probability of mutation (between 0 and 1).
            n (int): Distribution index for mutation.
            delta_max (float): Maximum allowed perturbation.
        """
        super().__init__(probability)
        self.n = n
        self.delta_max = delta_max

    def _mutate(self, individual: Individual, population: Population) -> Population:
        """
        Applies Deb & Goyal mutation to the individual's chromosome.

        Parameters:
            individual (Individual): A single individual to mutate.
            population (Population): The population containing individuals.

        Returns:
            Population: The population with mutated individuals.
        """
        num_offspring = len(population)

        for j in range(num_offspring):
            chromosome = population[j].chromosome

            for i in range(self.n):
                if np.random.uniform(0, 1) <= self.probability:
                    u = np.random.uniform(0, 1)

                    if u < 0.5:
                        delta = np.power(2 * u, 1 / (self.n + 1)) - 1
                    else:
                        delta = 1 - np.power(2 * (1 - u), 1 / (self.n + 1))

                    chromosome[i] += delta * self.delta_max

            population[j].chromosome = chromosome

        return population
