def click_to_file_format(filename: str, data: 'list'):
    """
    Adds lines to `filename` with [number] of line in front
    :param filename: file to append to
    :param data: Array [x, y, rand, mouse]
    :return: None
    """
    with open(filename, "a") as f:
        f.write('CLICK,{},{},{},{}\n'.format(data[0], data[1], data[2], data[3]))


def sleep_to_file_format(filename: str, time: int, rand: int = 0):
    with open(filename, "a") as f:
        f.write('SLEEP,{},{}\n'.format(time, rand))
