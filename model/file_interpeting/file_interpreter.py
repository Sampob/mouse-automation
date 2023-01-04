from threading import Event

from model.actions.action_man import ActionMan


class FileController:
    """
    Handles file reading and parsing
    """
    def __init__(self):
        self.filename = ''
        self.file_index = 0

    action_man = ActionMan()

    def set_filename(self, name: str):
        """
        Sets the file to be executed
        :param name: path and name of the file
        :return: None
        """
        self.filename = name

    def readfile(self, event: Event = None):
        """
        Opens file with `__filename` and reads lines one by one until through the file
        Passes each line to select_action which acts accordingly
        :return: None
        """
        with open(self.filename, 'r') as f:
            continue_loop = True
            nextline = None
            self.file_index = 0
            while nextline != '' and continue_loop and not event.is_set():
                nextline = f.readline()
                try:
                    if nextline[0] != '#' and nextline != '':
                        nextline = nextline[:len(nextline) - 1]
                        continue_loop = self.parse_action(nextline)
                except IndexError:
                    pass
                self.file_index += 1

    def parse_action(self, line: str):
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

        return self.action_man.select_action(selection).execute_action(values)
