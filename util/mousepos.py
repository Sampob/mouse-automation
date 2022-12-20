from pynput import keyboard
import pyautogui
import time
from threading import Thread


# pynput works in its own thread
# For every press of keyboard, calls 'on_press' function with the key pressed as parameter
def on_press(key):
    if key == keyboard.Key.esc:
        return False
    if key == keyboard.Key.insert or key == keyboard.Key.home:
        print(pyautogui.position())

    else:
        print('Received {}'.format(key))


# Sets function to be called on press
listener = keyboard.Listener(on_press=on_press)
listener.start()

listener.join()
print("Listener thread joined\nStopping...")
