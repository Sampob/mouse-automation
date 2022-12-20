from time import sleep
from random import randint


def delay(time, rand):
    """
    Adds specified or random delay to actions
    :param time: time in milliseconds to delay for
    :param rand: random variation to add to delay
    :return: None
    """
    time = (time + randint(-rand, rand)) / 1000
    print("Sleeping for: {}".format(time))
    sleep(time)
