import pyautogui


def locate_image(img: str):
    """
    Finds specified images center coordinates on screen
    Returns the first match from left to right, up to down
    :param img: image path and filename
    :return: Point with center coordinates or False if not found
    """
    try:
        return pyautogui.center(pyautogui.locateOnScreen(img))
    except TypeError:
        return False
