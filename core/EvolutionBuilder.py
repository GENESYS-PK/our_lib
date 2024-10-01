from typing import Type, Callable, List, Tuple, Self
from Selection import Selection
from Crossover import Crossover
from Mutation import Mutation
from OperatorsPreset import OperatorsPreset


class EvolutionBuilder:
    """
    A builder class for constructing an instance of the Evolution class. This class follows the
    builder pattern to ensure that all required parameters are properly set before the
    Evolution object is created.

    :param evolution_reference: A reference to the Evolution class, not an instance of the class.
    """

    def __init__(self, evolution_reference: Evolution = Evolution):
        """
        Initialize the EvolutionBuilder with a reference to the Evolution class.

        :param evolution_reference: A reference to the Evolution class (not an instance).
        """
        self.evolution_reference = evolution_reference
        self.selection = None
        self.crossover = None
        self.mutation = None
        self.elitism = None
        self.fitness_function = None
        self.population_generator = None
        self.events = []
        self.jobs = []
        self.terminator = None
        self.clamp_strategy = None
        self.population_size = None
        self.individual_size = None
        self.max_epoch = None
        self.maximize = None
        self.representation = None
        self.variable_domains = None

    def _validate(self, var, var_type, var_name):
        """
        Validate that a variable is of the expected type.

        :param var: The variable to validate.
        :param var_type: The expected type of the variable.
        :param var_name: The name of the variable (for error reporting).
        :raises ValueError: If the variable is not of the expected type.
        """
        if not isinstance(var, var_type):
            raise ValueError(f"{var_name} must be of type {var_type.__name__}")

    def set_selection(self, selection: Selection) -> Self:
        """
        Set the selection operator for the evolution process.

        :param selection: The selection operator to use.
        :return: The EvolutionBuilder instance, allowing for method chaining.
        """
        self._validate(selection, Selection, "Selection")
        self.selection = selection
        return self

    def set_crossover(self, crossover: Crossover) -> Self:
        """
        Set the crossover operator for the evolution process.

        :param crossover: The crossover operator to use.
        :return: The EvolutionBuilder instance, allowing for method chaining.
        """
        self._validate(crossover, Crossover, "Crossover")
        self.crossover = crossover
        return self

    def set_mutation(self, mutation: Mutation) -> Self:
        """
        Set the mutation operator for the evolution process.

        :param mutation: The mutation operator to use.
        :return: The EvolutionBuilder instance, allowing for method chaining.
        """
        self._validate(mutation, Mutation, "Mutation")
        self.mutation = mutation
        return self

    def use_preset(self, preset: OperatorsPreset) -> Self:
        """
        Set the selection, crossover, and mutation operators using a preset.

        :param preset: An OperatorsPreset instance with predefined operators.
        :return: The EvolutionBuilder instance, allowing for method chaining.
        """
        self.set_selection(preset.selection)
        self.set_crossover(preset.crossover)
        self.set_mutation(preset.mutation)
        return self

    def set_elitims(self, elitims: Elitism) -> Self:
        """
        Set the elitism strategy for the evolution process.

        :param elitims: The elitism strategy to use.
        :return: The EvolutionBuilder instance, allowing for method chaining.
        """
        self._validate(elitims, Elitism, "Elitism")
        self.elitism = elitims
        return self

    def set_fitness_function(self, fitness_function: FitnessFunction) -> Self:
        """
        Set the fitness function for the evolution process.

        :param fitness_function: The fitness function to use.
        :return: The EvolutionBuilder instance, allowing for method chaining.
        """
        self._validate(fitness_function, FitnessFunction, "Fitness Function")
        self.fitness_function = fitness_function
        return self

    def set_population_generator(
        self,
        population_function: Callable[[int, int], List[Tuple[(int, int)]]],
        population_size: int | None = None,
        individual_size: int | None = None,
        variable_domains: List[Tuple[(int, int)]] | None = None,
    ) -> Self:
        """
        Set the population generator for the evolution process.

        :param population_function: The function responsible for generating the population.
        :param population_size: The size of the population (optional).
        :param individual_size: The size of an individual (optional).
        :param variable_domains: The variable domains for generating individuals (optional).
        :return: The EvolutionBuilder instance, allowing for method chaining.
        """
        self._validate(population_function, Callable, "Population Generator")
        self.population_generator = population_function
        self.population_size = population_size
        self.individual_size = individual_size
        self.variable_domains = variable_domains
        return self

    def set_population_size(self, population_size: int) -> Self:
        """
        Set the population size for the evolution process.

        :param population_size: The number of individuals in the population.
        :return: The EvolutionBuilder instance, allowing for method chaining.
        """
        self._validate(population_size, int, "Population Size")
        self.population_size = population_size
        return self

    def set_individual_size(self, individual_size: int) -> Self:
        """
        Set the individual size for the evolution process.
        :param individual_size: The number of elements in an individual
        :return: The EvolutionBuilder instance, allowing for method chaining.
        """
        self._validate(individual_size, int, "Individual Size")
        self.individual_size = individual_size
        return self

    def set_generator_domain(self, domain: List[Tuple[int, int]]) -> Self:
        """
        Set the domain for generating individuals in the initial population.

        :param domain: A list of tuples representing the range of values for each variable.
        :return: The EvolutionBuilder instance, allowing for method chaining.
        """
        self._validate(domain, list, "Domain")
        self.variable_domains = domain
        return self

    def add_job(self, job: Job) -> Self:
        """
        Add a job to the list of jobs for the evolution process.

        :param job: The job to add.
        :return: The EvolutionBuilder instance, allowing for method chaining.
        """
        self._validate(job, Job, "Job")
        self.jobs.append(job)
        return self

    def add_event_listener(self, event_type: EventListenerType, event: Callable[EvolutionState]) -> Self:
        """
        Add an event listener for the evolution process.

        :param event_type: The type of event to listen for.
        :param event: The function to be called when the event occurs.
        :return: The EvolutionBuilder instance, allowing for method chaining.
        """
        self._validate(event, Callable, "Event")
        self.events.append((event_type, event))
        return self