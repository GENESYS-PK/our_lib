import numpy as np
from abc import ABC, abstractmethod


class Mutation(ABC):
    allowed_representation = []

    def __init__(self, probability: float = 0):
        self.probability = probability

    def mutate(self, population_parent: Population) -> Population:
        for individual in population_parent.population:
            if np.random.rand() < self.probability:
                self._mutate(individual, population_parent)

        return population_parent

    @abstractmethod
    def _mutate(self, individual: Individual, population: Population):
        pass
