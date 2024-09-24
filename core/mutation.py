class Mutation:
    def __init__(self, probability: float = 0):
        self.probability = probability
        self.allowedRepresentation = Representation()

    def mutate(self, population_parent: Population) - > Population:
        pass

    def _mutate(self, individual: Individual, population: Population) - > Population:
        pass

    