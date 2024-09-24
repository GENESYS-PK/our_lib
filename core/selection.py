class Selection:
    def __init__(self, target_population: int, maximize: bool):
        self.target_population = target_population
        self.maximize = maximize
        self.allowedRepresentation = Representation()

    def select(self, population: Population) -> Population:
        pass
    
    def _select(self, population: Population) -> Population:
        pass
