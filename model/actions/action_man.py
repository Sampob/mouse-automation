from model.actions.action_functions.click_action import ClickAction
from model.actions.action_functions.confirm_action import ConfirmAction
from model.actions.action_functions.execute_action import ExecuteAction
from model.actions.action_functions.key_action import KeyAction
from model.actions.action_functions.move_action import MoveAction
from model.actions.action_functions.sleep_action import SleepAction
from model.actions.action_functions.wait_color_action import WaitColorAction
from model.actions.action_interface import ActionInterface


# TODO Look into using enums

class ActionMan:
    """
    Finds the wanted action and calls it
    """

    def __init__(self):
        pass

    def select_action(self, string, values) -> ActionInterface:
        __return_value = None
        """
        Finds the action and calls its function
        :param string: action
        :param values: action parameters
        :return: Boolean to continue or not
        """
        if string == 'MOVE':
            __return_value = MoveAction()
        elif string == 'CLICK':
            __return_value = ClickAction()
        elif string == 'SLEEP':
            __return_value = SleepAction()
        elif string == 'CONFIRM':
            __return_value = ConfirmAction()
        elif string == 'WAIT COLOR':
            __return_value = WaitColorAction()
        elif string == 'WAIT COLOR AT':
            __return_value = WaitColorAction()
        elif string == 'EXECUTE':
            __return_value = ExecuteAction()
        elif string == 'KEY':
            __return_value = KeyAction()
        else:
            print("Action not recognized")
        return __return_value
