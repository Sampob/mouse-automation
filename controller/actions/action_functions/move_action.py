from controller.actions.action_interface import ActionInterface
from model.mouse.mouse_automation import move_mouse_to


class MoveAction(ActionInterface):

    def __init__(self):
        super().__init__('MOVE')

    def execute_action(self, values: list[int]) -> bool:
        """
        Move mouse to coordinates
        :param values: Array [x, y, rand]
        :return: True to continue
        """
        # move_mouse_to(x=None, y=None, arr=None, rand=0)
        move_mouse_to(x=int(values[0]), y=int(values[1]), rand=int(values[2]))
        return True
