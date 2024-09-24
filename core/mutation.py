from abc import ABC, abstractmethod

class Mutation(ABC):
    def __init__(self, probability: float = 0):
        self.probability = probability
        self.allowedRepresentation = Representation()

    def mutate(self, population_parent: Population) -> Population:
        
    @abstractmethod
    def _mutate(self, individual: Individual, population: Population) -> Population:
        pass

    