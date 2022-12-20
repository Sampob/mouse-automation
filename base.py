from pynput import keyboard
import time
import pyautogui as gui
from threading import Thread
import os

thread_bool = False


def threadfunc():
    global thread_bool

    print("Thread start")
    for i in range(5):
        time.sleep(1)
        print("Thread")
    print("Stopping")
    thread_bool = False


def on_press(key):
    global thread_bool

    if key == keyboard.Key.esc:
        return False

    if key == keyboard.Key.f6:
        if not thread_bool:
            t1 = Thread(target=threadfunc, args=())
            t1.start()
            thread_bool = not thread_bool
        else:
            print("Thread already running")

    else:
        print('Received event {}'.format(key))


listener = keyboard.Listener(on_press=on_press)
listener.start()

listener.join()
print("Listener thread joined")

print("Stopping")
