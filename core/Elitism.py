import numpy as np
from abc import ABC, abstractmethod
from Population import Population

class Elitism(ABC):
    """
    Abstract class providing a framework for elitism implementation.
    """

    def chooseElitism(self, population: Population) -> Population:
        """
        Perform chosen elitism strategy on population.
        :param population: A population on which elitism acts.
        :return: ***Population***
        """
        return self._performElitism(population)

    @abstractmethod
    def _performElitism(self, population: Population) -> Population:
        """
        Implementation of elitism strategy.
        :param population: A population on which elitism acts.
        :return: ***Population***
        """
        pass
