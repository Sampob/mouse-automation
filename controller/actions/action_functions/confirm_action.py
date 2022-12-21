import pyautogui

from controller.actions.action_interface import ActionInterface


class ConfirmAction(ActionInterface):

    def __init__(self):
        super().__init__('CONFIRM')

    def execute_action(self, values: list[str]) -> bool:
        """
        Prompts user to continue or stop
        :param values: Array [Text to continue, text to cancel]
        :return: Boolean to continue or stop
        """
        text = pyautogui.confirm(text='Continue?', buttons=[values[0], values[1]])
        if text == values[1]:
            return False
        return True
