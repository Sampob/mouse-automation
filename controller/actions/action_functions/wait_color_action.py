from controller.actions.action_interface import ActionInterface
from time import sleep

from model.image_matching.pixel_functions import compare_rgb, rgb_at, rgb_at_mouse


class WaitColorAction(ActionInterface):

    def __init__(self):
        super().__init__('WAIT COLOR')

    def execute_action(self, values: 'list') -> bool:
        """
        Wait for color at coordinates to continue
        :param values: Array [x, y, [r, g, b], tolerance, delay]
        :return: True to continue
        """
        color_continue = True
        while color_continue:
            if compare_rgb(color1=rgb_at(x=int(values[0]), y=int(values[1])),
                           color2=[int(values[2]), int(values[3]), int(values[4])], tolerance=int(values[5])):
                color_continue = False
            else:
                sleep(int(values[6]) / 1000)
        return True

    def execute_alt(self, values) -> bool:
        color_continue = True
        print(rgb_at_mouse())
        while color_continue:
            if compare_rgb(color1=rgb_at_mouse(), color2=[int(values[0]), int(values[1]), int(values[2])],
                           tolerance=int(values[3])):
                color_continue = False
            else:
                sleep(int(values[4]) / 1000)
        return True
