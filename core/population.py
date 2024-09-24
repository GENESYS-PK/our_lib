from dataclasses import dataclass, field
from typing import List
import singledispatch


@dataclass
class Population:
    population: List[Individual] = field(default_factory=list)

    @property
    def population_size(self) -> int:
        return len(self.population)

    @singledispatch
    def add_to_population(individual: Individual):
        self.population.append(individual)

    @singledispatch
    def add_to_population(individual_list: Iterable[Individual]):
        self.population.extend(individual_list)

    @singledispatch
    def add_to_population(individual_list: Population):
        self.population.extend(individual_list.population)

    def trim_children(how_many_keep: int):
        self.population = self.population[:how_many_keep]
