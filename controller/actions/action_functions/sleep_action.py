from controller.actions.action_interface import ActionInterface
from controller.operands.time import delay


class SleepAction(ActionInterface):

    def __init__(self):
        super().__init__('SLEEP')

    def execute_action(self, values: list[int]) -> bool:
        """
        Delays the following action
        :param values: Array [delay, rand]
        :return: Boolean to continue or stop
        """
        # delay(time, rand)
        delay(int(values[0]), int(values[1]))
        return True
