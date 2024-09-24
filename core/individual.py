from dataclasses import dataclass
from typing import Any


@dataclass
class Individual:
    """
    Klasa przechowująca dane o osobniku.

    :param chromosome: Chromosom reprezentujący osobnika (może być dowolnego typu).
    :param value: Wartość przystosowania dla tego osobnika, wyrażona jako liczba zmiennoprzecinkowa.
    """

    chromosome: Any
    value: float
