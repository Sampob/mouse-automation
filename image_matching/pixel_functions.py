import pyautogui


def rgb_at_mouse():
    """
    Gets the rgb values at current mouse position
    :return: Array [r, g, b]
    """
    x, y = pyautogui.position()
    r, g, b = pyautogui.pixel(x, y)
    return [r, g, b]


def rgb_at(x=None, y=None, arr=None):
    """
    Get the rgb values of any pixel on screen
    :param x: horizontal coordinate
    :param y: vertical coordinate
    :param arr: Array [x, y] with x and y coordinates
    :return: Array [r, g, b]
    """
    if x and y:
        r, g, b = pyautogui.pixel(x, y)
    elif arr:
        r, g, b = pyautogui.pixel(arr[0], arr[1])
    else:
        raise TypeError("Need x and y, or arr argument")
    return [r, g, b]


def compare_rgb(color1, color2, tolerance):
    """
    Compares two RGB colors
    'tolerance' dictates how far each value can be from the actual one
    E.g. compare_rgb([50, 50, 50], rgb_at_mouse(), 0) would return True
    if rgb value at mouse location is exactly 50, 50, 50
    :param color1: Array of RGB values of first color
    :param color2: Array of RGB values of second color
    :param tolerance: how much values can vary
    :return: Boolean of do colors match
    """
    return (color1[0] - tolerance <= color2[0] <= color1[0] + tolerance) and \
        (color1[1] - tolerance <= color2[1] <= color1[1] + tolerance) and \
        (color1[2] - tolerance <= color2[2] <= color1[2] + tolerance)
