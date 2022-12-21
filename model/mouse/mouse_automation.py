import pyautogui
from random import randint
from model.image_matching.image_functions import locate_image


def click_mouse_at(x=None, y=None, arr=None, rand=0, mouse='left'):
    """
    Click mouse at coordinates x, y
    `rand` adds random variation to coordinates from -rand to rand
    Random is calculated separately to both x and y value
    'mouse' specifies mouse button to click
    E.g. click_mouse_at(100, 100, 10, 'left') left clicks mouse at random position from 90, 90 to 110, 110
    :param arr: Array [x, y] with x and y coordinates
    :param x: horizontal position on screen
    :param y: vertical position on screen
    :param rand: position variation
    :param mouse: clicked mouse button
    :return: None
    """
    if x and y:
        pyautogui.click((x + randint(-rand, rand), (y + randint(-rand, rand))), button=mouse)
    elif arr:
        pyautogui.click((arr[0] + randint(-rand, rand), (arr[1] + randint(-rand, rand))), button=mouse)
    else:
        raise TypeError("Need x and y, or arr argument")


def click_mouse(x=None, y=None, arr=None, rand=0, mouse='left'):
    """
    Clicks mouse from current position by x and y
    `rand` adds random variation to movement
    Random is calculated separately to both x and y value
    'mouse' specifies mouse button to click
    E.g. click_mouse(0, 0, 0, 'left') left clicks mouse at current location
    :param arr: Array [x, y] with x and y coordinates
    :param x: horizontal position on screen
    :param y: verical position on screen
    :param rand: position variation
    :param mouse: clicked mouse button
    :return: None
    """
    if x and y:
        move_mouse(x, y, rand)
    elif arr:
        move_mouse(arr[0], arr[1])
    else:
        raise TypeError("Need x and y, or arr argument")
    pyautogui.click(button=mouse)


def move_mouse_to(x=None, y=None, arr=None, rand=0):
    """
    Move mouse to coordinates x, y
    `rand` adds random variation to coordinates from -rand to rand
    Random is calculated separately to both x and y value
    E.g. move_mouse_to(100, 100, 10) moves mouse to a random position from 90, 90 to 110, 110
    :param arr: Array [x, y] with x and y coordinates
    :param x: horizontal position on screen
    :param y: vertical position on screen
    :param rand: position variation
    :return: None
    """
    if x and y:
        pyautogui.moveTo((x + randint(-rand, rand), (y + randint(-rand, rand))))
    elif arr:
        pyautogui.moveTo((arr[0] + randint(-rand, rand), (arr[1] + randint(-rand, rand))))
    else:
        raise TypeError("Need x and y, or arr argument")


def move_mouse(x=None, y=None, arr=None, rand=0):
    """
    Move mouse from current position by x and y
    `rand` adds random variation to movement
    E.g. move_mouse(0, 0, 5) adds a tiny random movement to current position
    :param arr: Array [x, y] with x and y coordinates
    :param x: horizontal position on screen
    :param y: vertical position on screen
    :param rand: position variation
    :return: None
    """
    cur_x, cur_y = pyautogui.position()
    if x and y:
        pyautogui.moveTo((cur_x + x + randint(-rand, rand)), (cur_y + y + randint(-rand, rand)))
    elif arr:
        pyautogui.moveTo((cur_x + arr[0] + randint(-rand, rand)), (cur_y + arr[1] + randint(-rand, rand)))
    else:
        raise TypeError("Need x and y, or arr argument")


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


def click_at_image(img, mouse='left'):
    """
    Uses other functions to find and click specified image
    :param img: image path and filename
    :param mouse: mouse action to perform
    :return: None
    """
    click_mouse_at(arr=point_to_coordinates(locate_image(img)), mouse=mouse)
