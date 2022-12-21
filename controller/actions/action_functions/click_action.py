from controller.actions.action_interface import ActionInterface
from model.mouse.mouse_automation import click_mouse, click_mouse_at


class ClickAction(ActionInterface):

    def __init__(self):
        super().__init__('CLICK')

    def execute_action(self, values: list[int]) -> bool:
        """
        Click mouse at coordinates
        :param values: Array [x, y, rand, mouse]
        :return: True to continue
        """
        if len(values) == 2:
            # click_mouse(x, y, rand, mouse)
            click_mouse(0, 0, int(values[0]), values[1])
        elif len(values) == 4:
            # click_mouse_at(x, y, rand, mouse)
            click_mouse_at(int(values[0]), int(values[1]), int(values[2]), values[3])
        return True
