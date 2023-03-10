from model.actions.action_interface import ActionInterface
from model.operands.time import delay


class SleepAction(ActionInterface):

    def __init__(self):
        super().__init__('SLEEP')

    def execute_action(self, values) -> bool:
        """
        Delays the following action
        :param values: Array [delay, rand]
        :return: Boolean to continue or stop
        """
        # delay(time, rand=0)
        delay(int(values[0]), rand=int(values[1]))
        return True
