from typing import List, Union
from Condition import Condition
from Concatenator import Concatenator


class Expression(Condition):
    """
    Represents a logical expression made up of conditions and concatenators.

    This class allows for the construction of complex logical expressions
    that can be evaluated as part of an evolution process.
    """

    def __init__(self):
        """
        Initialize the Expression class with an empty expression list.
        """
        super().__init__()
        self.expression_list: List[Condition|Concatenator] = []

    def evaluate(self, evolution) -> bool:
        """
        Evaluate the logical expression based on the provided evolution instance.

        The method parses the expression list and applies the logical operators
        (AND/OR) between the conditions.

        :param evolution: The evolution process instance to evaluate.
        :return: A boolean representing the result of the logical expression.
        :raises ValueError: If the expression list is empty.
        """
        if not self.expression_list:
            raise ValueError("Expression list is empty.")

        # Initialize with the evaluation of the first condition
        result = self.expression_list[0].evaluate(evolution)

        # Parse through the expression list
        for i in range(1, len(self.expression_list), 2):
            concatenator = self.expression_list[i]
            next_condition = self.expression_list[i + 1]

            if concatenator == Concatenator.AND:
                result = result and next_condition.evaluate(evolution)
            elif concatenator == Concatenator.OR:
                result = result or next_condition.evaluate(evolution)

        return result

    def begin(self, condition: Condition) -> 'Expression':
        """
        Begin the logical expression with the first condition.

        :param condition: The initial condition or sub-expression to add.
        :return: The Expression instance, allowing for method chaining.
        :raises ValueError: If the expression has already been started.
        """
        if self.expression_list:
            raise ValueError("Expression already started with a condition.")

        self.expression_list.append(condition)
        return self

    def and_(self, condition: Condition) -> 'Expression':
        """
        Add a condition to the expression with an AND operator.

        :param condition: The condition or sub-expression to add.
        :return: The Expression instance, allowing for method chaining.
        :raises ValueError: If no initial condition exists in the expression.
        """
        if not self.expression_list:
            raise ValueError("Expression must begin with a condition.")

        self.expression_list.append(Concatenator.AND)
        self.expression_list.append(condition)
        return self

    def or_(self, condition: Condition) -> 'Expression':
        """
        Add a condition to the expression with an OR operator.

        :param condition: The condition or sub-expression to add.
        :return: The Expression instance, allowing for method chaining.
        :raises ValueError: If no initial condition exists in the expression.
        """
        if not self.expression_list:
            raise ValueError("Expression must begin with a condition.")

        self.expression_list.append(Concatenator.OR)
        self.expression_list.append(condition)
        return self
