from controller.actions.action_interface import ActionInterface
from model.mouse.mouse_automation import click_mouse, click_mouse_at


class ClickAction(ActionInterface):

    def __init__(self):
        super().__init__('CLICK')

    def execute_action(self, values) -> bool:
        print(values)
        """
        Click mouse at coordinates
        :param values: Array [x, y, rand, mouse]
        :return: True to continue
        """
        if len(values) == 2:
            # click_mouse(x=None, y=None, arr=None, rand=0, mouse='left')
            click_mouse(x=0, y=0, rand=int(values[0]), mouse=values[1])
        elif len(values) == 3:
            # click_mouse(x=None, y=None, arr=None, rand=0, mouse='left')
            click_mouse_at(x=int(values[0]), y=int(values[1]), rand=int(values[2]))
        elif len(values) == 4:
            # click_mouse(x=None, y=None, arr=None, rand=0, mouse='left')
            click_mouse_at(x=int(values[0]), y=int(values[1]), rand=int(values[2]), mouse=values[3])
        return True
