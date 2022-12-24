def click_to_file_format(filename: str, data: 'list'):
    """
    Adds lines to `filename` with [number] of line in front
    :param filename: file to append to
    :param data: Array [x, y, rand, mouse]
    :return: None
    """
    with open(filename, "a") as f:
        f.write('CLICK,{},{},{},{}\n'.format(data[0], data[1], data[2], data[3]))


def sleep_to_file_format(filename: str, time: str, rand: int = 0):
    with open(filename, "a") as f:
        f.write('SLEEP,{},{}\n'.format(time, rand))


def key_to_file_format(filename: str, key: str):
    with open(filename, "w") as f:
        f.write('KEY,{}'.format(key))
