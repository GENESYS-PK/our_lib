import numpy as np
from abc import ABC, abstractmethod
from population import Population

class Crossover(ABC):
    allowed_representation = []

    def __init__(self, how_many_individuals: int, probability: float = 0):
        self.how_many_individuals = how_many_individuals
        self.probability = probability

    def cross(self, population_parent: Population) -> Population:
        offspring = Population()

        while offspring.population_size < population_parent.population_size:
            if np.random.rand() < self.probability:
                offspring.add_to_population(self._cross(population_parent))

        offspring.trim_children(self.how_many_individuals)
        return offspring

    @abstractmethod
    def _cross(self, population_parent: Population) -> Population:
        pass
