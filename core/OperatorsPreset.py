from dataclasses import dataclass
from Mutation import Mutation
from Crossover import Crossover
from Selection import Selection


@dataclass
class OperatorsPreset:
    selection: Selection|None = None
    crossover: Crossover|None = None
    mutation: Mutation|None = None
