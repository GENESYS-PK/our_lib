from Mutation import Mutation
from Selection import Selection
from Crossover import Crossover
from Elitism import Elitism
from FitnessFunction import FitnessFunction
from Job import Job
from Population import Population
from Expression import Expression
from EvolutionState import EvolutionState
from EventListenerType import EventListenerType
from OperatorsPreset import OperatorsPreset


from typing import List, Tuple, Callable, Self


class Evolution:
    def __init__(
        self,
        mutation: Mutation,
        selection: Selection,
        crossover: Crossover,
        elitism: Elitism,
        fitness_function: FitnessFunction,
        job_queue: List[Job],
        init_population: Population,
        population_size: int,
        terminator: Expression,
        maximize: bool,
        events: Tuple[List[Callable[[EvolutionState], None]], ...],
    ):
        self.mutation = mutation
        self.selection = selection
        self.crossover = crossover
        self.elitism = elitism
        self.fitness_function = fitness_function
        self.job_queue = job_queue
        self.terminator = terminator
        self.evolution_state = EvolutionState()
        self.terminate_loop: bool = False
        self.events = events
        self.representation = []
        self.population = init_population
        self.population_size = population_size
        self.maximize = maximize

    def set_selection(self, selection: Selection) -> Self:
        self.selection = selection
        return self
    
    def set_crossover(self, crossover: Crossover) -> Self:
        self.crossover = crossover
        return self

    def set_mutation(self, mutation: Mutation) -> Self:
        self.mutation = mutation
        return self

    def use_preset(self, preset: OperatorsPreset) -> Self:
        self.selection = preset.selection
        self.crossover = preset.crossover
        self.mutation = preset.mutation
        return self

    def run(self) -> None:
        pass
    
    def loop(self) -> None:
        pass

    def get_evolution_state(self) -> EvolutionState:
        pass

    def crossover(self) -> None:
        pass

    def selection(self) -> None:
        pass

    def mutation(self) -> None:
        pass

    def elitism(self) -> None:
        pass