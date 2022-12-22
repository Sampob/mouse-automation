from controller.actions.action_functions.click_action import ClickAction
from controller.actions.action_functions.confirm_action import ConfirmAction
from controller.actions.action_functions.execute_action import ExecuteAction
from controller.actions.action_functions.move_action import MoveAction
from controller.actions.action_functions.sleep_action import SleepAction
from controller.actions.action_functions.wait_color_action import WaitColorAction


# TODO Look into using enums

class ActionMan:
    """
    Finds the wanted action and calls it
    """

    def __init__(self):
        pass

    def select_action(self, string, values) -> bool:
        __return_value = True
        """
        Finds the action and calls its function
        :param string: action
        :param values: action parameters
        :return: Boolean to continue or not
        """
        if string == 'MOVE':
            __return_value = MoveAction().execute_action(values)
        elif string == 'CLICK':
            print("Click")
            __return_value = ClickAction().execute_action(values)
        elif string == 'SLEEP':
            __return_value = SleepAction().execute_action(values)
        elif string == 'CONFIRM':
            __return_value = ConfirmAction().execute_action(values)
        elif string == 'WAIT COLOR':
            __return_value = WaitColorAction().execute_action(values)
        elif string == 'WAIT COLOR AT':
            __return_value = WaitColorAction().execute_alt(values)
        elif string == 'EXECUTE':
            __return_value = ExecuteAction().execute_action(values)
        else:
            print("Action not recognized")
        return __return_value
