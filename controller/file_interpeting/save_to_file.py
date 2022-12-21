def append_to_file_format(filename, data, rand=0):
    """
    Adds lines to `filename` with [number] of line in front
    :param filename: file to append to
    :param data: text to add
    :param rand: random deviation to add
    :return: None
    """
    with open(filename, "a") as f:
        f.write('CLICK,{},{},{},{}\n'.format(data[0], data[1], data[2], data[3]))
