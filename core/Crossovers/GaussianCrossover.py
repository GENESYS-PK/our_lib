import numpy as np
import random, math
from core import Crossover, Individual, Population


class GaussCrossover(Crossover):
    """
    A class that implements the Gaussian crossover mechanism.

    :param xp: Lower bound for values.
    :param xk: Upper bound for values.
    """
    def __init__(self, how_many_individuals: int, probability: float = 0, xp: int = 5, xk: int = 10):
        super().__init__(how_many_individuals, probability)
        self.xp = xp
        self.xk = xk

    def _cross(self, population_parent: Population) -> Population:
        """
        Perform Gaussian crossover between two individuals from the parent population.

        :param population_parent: The population to perform the crossover operation on.
        :returns: The offspring population.
        """
        # Wybierz dwóch rodziców z populacji
        parent1, parent2 = population_parent.select_two()

        size = min(len(parent1), len(parent2))
        ind3 = []
        ind4 = []
        for i in range(size):
            odl = math.fabs(parent1[i] - parent2[i])
            a = random.random()
            if random.uniform(0, 1) <= 0.5:
                new_val1 = parent1[i] + a * (odl / 3)
                new_val2 = parent2[i] + a * (odl / 3)
            else:
                new_val1 = parent2[i] + a * (odl / 3)
                new_val2 = parent1[i] + a * (odl / 3)

            # Sprawdzenie ograniczeń
            if new_val1 < self.xp or new_val1 > self.xk:
                new_val1 = parent1[i]
            if new_val2 < self.xp or new_val2 > self.xk:
                new_val2 = parent2[i]

            ind3.append(new_val1)
            ind4.append(new_val2)

        # Utwórz nową populację potomków
        offspring = Population()
        offspring.add_to_population([ind3, ind4])

        return offspring