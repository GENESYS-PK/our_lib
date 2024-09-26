from typing import Type, Callable, List, Tuple, Self
from selection import Selection
from crossover import Crossover
from mutation import Mutation




class EvolutionBuilder:
    def __init__(self, evolution_reference: Type[Evolution]):
        self.evolution_reference = evolution_reference
        self.selection = None
        self.crossover = None
        self.mutation = None
        # self.elitism = Elitism()
        # self.fitness_function = None
        # self.population_generator = None
        # self.population_size = None
        # self.individual_size = None
        # self.events = []
        # self.jobs = []
        # self.terminator = None
        # self.clamp_strategy = ClampStrategy()
        # self.max_epoch = None
        # self.maximize = False
        # self.representation = Representation()

    def set_selection(self, selection: Selection) -> Self:
        if not isinstance(selection, Selection):
            raise TypeError("Invalid type for selection")
        self.selection = selection
        return self

    def set_crossover(self, crossover: Crossover) -> Self:
        if not isinstance(crossover, Crossover):
            raise TypeError("Invalid type for crossover")
        self.crossover = crossover
        return self

    def set_mutation(self, mutation: Mutation) -> Self:
        if not isinstance(mutation, Mutation):
            raise TypeError("Invalid type for mutation")
        self.mutation = mutation
        return self