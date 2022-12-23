from model.actions.action_interface import ActionInterface
from pynput.keyboard import Controller


class KeyAction(ActionInterface):

    def __init__(self):
        super().__init__('KEY')
        self.__controller = Controller()

    def execute_action(self, values) -> bool:
        """
        Press specified key
        :param values: key to press
        :return: bool to continue or stop
        """
        for i in values:
            self.__controller.tap(i)
        return True
