from abc import ABC, abstractmethod


class ActionInterface(ABC):
    def __init__(self, name='NULL'):
        self.command_name = name

    @abstractmethod
    def execute_action(self, *values) -> bool:
        """
        Execute the defined action
        :return: bool of whether to continue or not
        """
        return True

    def __str__(self) -> str:
        return self.command_name
