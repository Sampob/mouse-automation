from controller.actions.action_man import ActionMan


class FileController:
    """
    Handles file reading and parsing
    """
    def __init__(self):
        pass

    action_man = ActionMan()
    __filename = ''

    def set_filename(self, name):
        """
        Sets the file to be executed
        :param name: path and name of the file
        :return: None
        """
        self.__filename = name

    def readfile(self):
        """
        Opens file with `__filename` and reads lines one by one until through the file
        Passes each line to select_action which acts accordingly
        :return: None
        """
        with open(self.__filename, 'r') as f:
            continue_loop = True
            nextline = None
            while nextline != '' and continue_loop:
                nextline = f.readline()
                try:
                    if nextline[0] != '#' and nextline != '':
                        nextline = nextline[:len(nextline) - 1]
                        continue_loop = self.parse_action(nextline)
                except IndexError:
                    pass
        print("Stopping")

    def parse_action(self, line):
        """
        Gets a String type line
        Separates the action from parameters, selects it and passes it
        Current actions:
        MOVE - Moves mouse cursor to coordinates
        CLICK - Click mouse at current location or at coordinates
        SLEEP - Delays the following action
        CONFIRM - Prompts user to continue or stop
        :param line: String line to go through
        :return: Boolean of whether to continue or stop
        """
        selection = line.split(',')[0]
        values = line.split(',')[1:len(line)]

        return self.action_man.select_action(selection, values)
