import pyautogui


def confirm_action(values):
    text = pyautogui.confirm(text='Continue?', buttons=[values[0], values[1]])
    if text == values[1]:
        return False
    return True
