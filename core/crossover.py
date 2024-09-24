class Crossover:
    def __init__(self, how_many_individuals: int, probability: float = 0):
        self.how_many_individuals = how_many_individuals
        self.probability = probability
        self.allowedRepresentation = Representation()

    def cross(self, population_parent: Population) -> Population:
        pass

    def _cross(self, population_parent: Population) -> Population:
        pass