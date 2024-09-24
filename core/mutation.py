import numpy as np
from abc import ABC, abstractmethod


class Mutation(ABC):
    def __init__(self, probability: float = 0):
        self.probability = probability
        self.allowedRepresentation = Representation()

    def mutate(self, population_parent: Population) -> Population:
        offspring = Population()

        for individual in population_parent.population:
            if np.random.rand() < self.probability:
                offspring.add_to_population(self._mutate(individual, population_parent))

        # offspring.trim_children(population_parent.population_size)
        return offspring

    @abstractmethod
    def _mutate(self, individual: Individual, population: Population) -> Population:
        pass
