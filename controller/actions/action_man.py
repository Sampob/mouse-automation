import pyautogui

from controller.operands.time import delay
from model.mouse.mouse_automation import move_mouse_to, click_mouse, click_mouse_at


class ActionMan:
    """
    Finds the wanted action and calls it
    """

    def __init__(self):
        pass

    def select_action(self, string, values):
        """
        Uses a switch case to find the action and calls its function
        :param string: action
        :param values: action parameters
        :return: Boolean to continue or not
        """
        if string == 'MOVE':
            return self.move_action(values)
        elif string == 'CLICK':
            return self.click_action(values)
        elif string == 'SLEEP':
            return self.sleep_action(values)
        elif string == 'CONFIRM':
            return self.confirm_action(values)
        else:
            return self.confirm_action(['Continue', 'Stop'], text='Invalid action, continue?')

    def move_action(self, values):
        # move_mouse_to(x=None, y=None, arr=None, rand=0)
        move_mouse_to(int(values[0]), int(values[1]), int(values[2]))
        return True

    def click_action(self, values):
        if len(values) == 2:
            # click_mouse(x, y, rand, mouse)
            click_mouse(0, 0, int(values[0]), values[1])
        elif len(values) == 4:
            # click_mouse_at(x, y, rand, mouse)
            click_mouse_at(int(values[0]), int(values[1]), int(values[2]), values[3])
        return True

    def sleep_action(self, values):
        # delay(time, rand)
        delay(int(values[0]), int(values[1]))
        return True

    def confirm_action(self, values, text='Continue?'):
        text = pyautogui.confirm(text=text, buttons=[values[0], values[1]])
        if text == values[1]:
            return False
        return True
