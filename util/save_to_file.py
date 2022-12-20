def append_to_file(filename, data):
    """
    Adds lines to `filename` with [number] of line in front
    :param filename: file to append to
    :param data: text to add
    :return: None
    """
    with open(filename, "a+") as f:
        f.seek(0)
        index = len(f.readlines())
        f.write('[{}] {}\n'.format((index + 1), data))
