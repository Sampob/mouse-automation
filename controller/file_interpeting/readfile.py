from model.mouse.mouse_automation import *
from controller.operands.time import *


def readfile(filename):
    """
    Opens file with 'filename' and reads lines one by one until through the file
    Passes each line to select_action which acts accordingly
    :param filename: file to go through
    :return: None
    """
    with open(filename, 'r') as f:
        con = True
        nextline = None
        while nextline != '' and con:
            nextline = f.readline()
            try:
                if nextline[0] != '#' and nextline != '':
                    nextline = nextline[:len(nextline) - 1]
                    con = select_action(nextline)
            except IndexError:
                pass
    print("Stopping")


def select_action(line):
    """
    Gets a String type line
    Separates the action from parameters, selects it and passes parameters
    Current actions:
    MOVE - Moves mouse cursor to coordinates
    CLICK - Click mouse at current location or at coordinates
    SLEEP - Delays the following action
    CONFIRM - Prompts user to continue or stop
    :param line: String line to go through
    :return: Boolean of whether to continue or stop
    """
    selection = line.split(',')[0]
    values = line.split(',')[1:len(line)]

    if selection == 'MOVE':
        # move_mouse_to(x, y, rand)
        move_mouse_to(int(values[0]), int(values[1]), int(values[2]))

    elif selection == 'CLICK':
        if len(values) == 2:
            # click_mouse(x, y, rand, mouse)
            click_mouse(0, 0, int(values[0]), values[1])
        elif len(values) == 4:
            # click_mouse_at(x, y, rand, mouse)
            click_mouse_at(int(values[0]), int(values[1]), int(values[2]), values[3])

    elif selection == 'SLEEP':
        # sleeping(time, rand)
        delay(int(values[0]), int(values[1]))

    elif selection == 'CONFIRM':
        text = pyautogui.confirm(text='Continue?', buttons=[values[0], values[1]])
        if text == values[1]:
            return False
    return True
