from abc import ABC, abstractmethod


class Selection(ABC):
    allowed_representation = []

    def __init__(self, target_population: int, maximize: bool):
        self.target_population = target_population
        self.maximize = maximize

    def select(self, population: Population) -> Population:
        selected_population = self._select(population)

        population.trim_children(self.target_population)
        return selected_population

    @abstractmethod
    def _select(self, population: Population) -> Population:
        pass
