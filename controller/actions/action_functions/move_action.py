from model.mouse.mouse_automation import move_mouse_to


def move_action(values):
    # move_mouse_to(x, y, rand)
    move_mouse_to(int(values[0]), int(values[1]), int(values[2]))
