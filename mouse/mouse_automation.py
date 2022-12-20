import pyautogui
from random import randint


def click_mouse_at(x, y, rand, mouse):
    """
    Click mouse at coordinates x, y
    'rand' adds random variation to coordinates from -rand to rand
    Random is calculated separately to both x and y value
    'mouse' specifies mouse button to click
    E.g. click_mouse_at(100, 100, 10, 'left') left clicks mouse at random position from 90, 90 to 110, 110
    :param x: horizontal position on screen
    :param y: vertical position on screen
    :param rand: position variation
    :param mouse: clicked mouse button
    :return:
    """
    pyautogui.click((x + randint(-rand, rand), (y + randint(-rand, rand))), button=mouse)


def click_mouse(x, y, rand, mouse):
    """
    Clicks mouse from current position by x and y
    rand adds random variation to movement
    Random is calculated separately to both x and y value
    'mouse' specifies mouse button to click
    E.g. click_mouse(0, 0, 0, 'left') left clicks mouse at current location
    :param x: horizontal position on screen
    :param y: verical position on screen
    :param rand: position variation
    :param mouse: clicked mouse button
    :return: None
    """
    move_mouse(x, y, rand)
    pyautogui.click(button=mouse)


def move_mouse_to(x, y, rand):
    """
    Move mouse to coordinates x, y
    rand adds random variation to coordinates from -rand to rand
    Random is calculated separately to both x and y value
    E.g. move_mouse_to(100, 100, 10) moves mouse to a random position from 90, 90 to 110, 110
    :param x: horizontal position on screen
    :param y: vertical position on screen
    :param rand: position variation
    :return: None
    """
    pyautogui.moveTo((x + randint(-rand, rand), (y + randint(-rand, rand))))


def move_mouse(x, y, rand):
    """
    Move mouse from current position by x and y
    rand adds random variation to movement
    With move_mouse(0, 0, 5) adds a tiny random movement to current position
    :param x: horizontal position on screen
    :param y: vertical position on screen
    :param rand: position variation
    :return: None
    """
    cur_x, cur_y = pyautogui.position()
    pyautogui.moveTo((cur_x + x + randint(-rand, rand)), (cur_y + y + randint(-rand, rand)))


def point_to_coordinates(point):
    """
    Formats Point object to an Array
    :param point: Point object with attributes x and y
    :return: Array [x, y], if no coordinates False
    """
    try:
        return [point.x, point.y]
    except AttributeError:
        return False
