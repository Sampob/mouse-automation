from controller.actions.action_functions.click_action import ClickAction
from controller.actions.action_functions.confirm_action import ConfirmAction
from controller.actions.action_functions.move_action import MoveAction
from controller.actions.action_functions.sleep_action import SleepAction
from controller.actions.action_interface import ActionInterface


class ActionMan:
    """
    Finds the wanted action and calls it
    """

    def __init__(self):
        pass

    def select_action(self, string, values):
        action = ActionInterface()
        """
        Finds the action and calls its function
        :param string: action
        :param values: action parameters
        :return: Boolean to continue or not
        """
        if string == 'MOVE':
            action = MoveAction()
        elif string == 'CLICK':
            action = ClickAction()
        elif string == 'SLEEP':
            action = SleepAction()
        elif string == 'CONFIRM':
            action = ConfirmAction()
        else:
            print("Action not recognized")
        return action.execute_action(string, values)
