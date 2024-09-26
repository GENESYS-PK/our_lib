from dataclasses import dataclass
from mutation import Mutation
from crossover import Crossover
from selection import Selection

@dataclass
class OperatorsPreset:
    selection: Selection = Selection(1,True)
    crossover: Crossover = Crossover(1)
    mutation: Mutation = Mutation()

