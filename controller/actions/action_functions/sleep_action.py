from controller.operands.time import delay


def sleep_action(values):
    # delay(time, rand)
    delay(int(values[0]), int(values[1]))