from typing import Type, Callable, List, Tuple, Self
from selection import Selection
from crossover import Crossover
from mutation import Mutation


class EvolutionBuilder:
    """
    A builder class for constructing an instance of the Evolution class. This class follows the
    builder pattern to ensure that all required parameters are properly set before the
    Evolution object is created.

    :param evolution_reference: A reference to the Evolution class, not an instance of the class.
    """

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
        """
        Set the selection operator for the evolution process.

        :param selection: The selection operator to use.
        :return: The EvolutionBuilder instance, allowing for method chaining.
        """
        if not isinstance(selection, Selection):
            raise TypeError("Invalid type for selection")
        self.selection = selection
        return self

    def set_crossover(self, crossover: Crossover) -> Self:
        """
        Set the crossover operator for the evolution process.

        :param crossover: The crossover operator to use.
        :return: The EvolutionBuilder instance, allowing for method chaining.
        """
        if not isinstance(crossover, Crossover):
            raise TypeError("Invalid type for crossover")
        self.crossover = crossover
        return self

    def set_mutation(self, mutation: Mutation) -> Self:
        """
        Set the mutation operator for the evolution process.

        :param mutation: The mutation operator to use.
        :return: The EvolutionBuilder instance, allowing for method chaining.
        """
        if not isinstance(mutation, Mutation):
            raise TypeError("Invalid type for mutation")
        self.mutation = mutation
        return self
