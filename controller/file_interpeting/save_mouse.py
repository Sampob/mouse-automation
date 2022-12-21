from pynput import mouse, keyboard

key_started = False
mouse_listener = None


def on_press(key):
    global key_started
    global mouse_listener
    if key == keyboard.Key.esc:
        return False
    elif key == keyboard.Key.right:
        if not key_started:
            print("Mouse started")
            mouse_listener = mouse.Listener(on_click=on_click)
            mouse_listener.start()
            key_started = not key_started
        elif key_started:
            print("Mouse stopped")
            mouse_listener.join()
            key_started = not key_started
    else:
        print(key)


def on_click(x, y, button, pressed):
    if pressed:
        mouse_button = ''
        if not 4 % button.value[0]:
            mouse_button = 'left'
            print("left")
        elif not 8 % button.value[1]:
            mouse_button = 'right'
            print("right")
        elif not 32 % button.value[1]:
            mouse_button = 'middle'
            print("middle")
        else:
            print("Unknown mouse button")
    # append_to_file_format(key[0], key[1], )


"""
(1761, 61, <Button.left: (4, 2, 0)>, True)
(1761, 61, <Button.left: (4, 2, 0)>, False)
"""

keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

keyboard_listener.join()
