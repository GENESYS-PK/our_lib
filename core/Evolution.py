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
        elitims: Elitism,
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
        self.init_population = init_population
        self.population_size = population_size
        self.terminator = terminator
        self.maximize = maximize
        self.events = events

    def set_selection(self, selection: Selection) -> Self:
        self.selection = selection

    def set_crossover(self, crossover: Crossover) -> Self:
        self.crossover = crossover

    def set_mutation(self, mutation: Mutation) -> Self:
        self.mutation = mutation

    def use_preset(self, preset: OperatorsPreset) -> Self:
        self.selection = preset.selection
        self.crossover = preset.crossover
        self.mutation = preset.mutation

    def add_event_listener(
        self, event_type: EventListenerType, event: Callable[EvolutionState]
    ) -> Self:
        pass

    def remove_event_listener(
        self, event_type: EventListenerType, event: Callable[EvolutionState]
    ) -> Self:
        pass

    def run(self) -> None:
        pass

    def loop(self) -> None:
        pass

    def get_evolution_state() -> EvolutionState:
        pass

    def crossover(self) -> None:
        pass

    def selection(self) -> None:
        pass

    def mutation(self) -> None:
        pass

    def elitism(self) -> None:
        pass

    def stepX(self) -> None:
        pass

    def hook(self, event_type: EventListenerType) -> None:
        pass
