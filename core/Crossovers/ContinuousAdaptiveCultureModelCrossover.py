import random
from core import Crossover, Individual, Population


class ContinuousAdaptiveCultureModelCrossover(Crossover):
    """
    Implements Continuous Adaptive Culture Model Crossover method which creates offspring based on the environment from one parent
    :param how_many_individuals: The number of individuals to create in the offspring.
    :param probability: The probability of performing the crossover operation.
    :param scaling_constant: Aa constant that controls the "distance" of the offspring from the parent.
                            Increasing the value of this constant increases the probability that the
                            offspring will be significantly "distanced" from the parent.
    """

    allowed_representation = []

    def __init__(self, how_many_individuals: int, scaling_constant: float, probability: float = 0):
        super().__init__(how_many_individuals, probability)
        self.scaling_constant = scaling_constant

    def cross(self, population_parent: Population) -> Population:
        """
        Perform the crossover operations for the entire population.

        :param population_parent: The population to perform the crossover operation on.
        :returns: The offspring population.
        """
        offspring = Population()

        while offspring.population_size < population_parent.population_size:
            if np.random.rand() < self.probability:
                offspring.add_to_population(self._cross(population_parent))

        offspring.trim_children(self.how_many_individuals)
        return offspring

    def _cross(self, population_parent: Population) -> Population:
        """
        :param population_parent: The population to perform the crossover operation on.
        :returns: The offspring.
        """

        parent_1, parent_2 = random.sample(population_parent.population, 2)

        probability_of_parent_selection = random.uniform(0, 1)
        offspring = []
        if probability_of_parent_selection < 0.5:
            for i in range(len(parent_1)):
                alfa = random.uniform(-0.5, 0.5)
                offspring.append(parent_1[i] + self.scaling_constant * alfa)
        elif probability_of_parent_selection >= 0.5:
            for i in range(len(parent_2)):
                alfa = random.uniform(-0.5, 0.5)
                offspring.append(parent_2[i] + self.scaling_constant * alfa)
        return offspring