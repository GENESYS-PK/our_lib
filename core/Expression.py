from typing import List, Self
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

    def evaluate(self, evolution: Self) -> bool:
        """
        Evaluate the logical expression based on the provided evolution instance.

        :param evolution: The evolution process instance to evaluate.
        :return: A boolean indicating the result of the logical expression.
        """
        if not self.expression_list:
            raise ValueError("The expression list is empty.")

        result = None
        current_condition = None
        current_concatenator = None

        for element in self.expression_list:
            if isinstance(element, Condition):
                # Evaluate the current condition
                current_result = element.evaluate(evolution)

                if result is None:
                    result = current_result
                else:
                    if current_concatenator == Concatenator.AND:
                        result = result and current_result
                    elif current_concatenator == Concatenator.OR:
                        result = result or current_result

                current_condition = element

            elif isinstance(element, Concatenator):
                # Set the current concatenator
                current_concatenator = element

        return result

    def begin(self, condition: Condition) -> Self:
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

    def and_(self, condition: Condition) -> Self:
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

    def or_(self, condition: Condition) -> Self:
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
