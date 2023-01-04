from threading import Event

from model.file_interpeting.file_interpreter import FileController


class ModelController:
    def __init__(self):
        self.fc = FileController()

    def set_script(self, script):
        self.fc.set_filename(script)

    def execute_script(self, loop: bool = False, times: int = None, event: Event = None):
        if loop:
            while True:
                self.fc.readfile(event=event)
        elif times and times > 0:
            for i in range(times):
                self.fc.readfile(event=event)
        else:
            print("NEG")

    def get_file_controller(self):
        return self.fc

    def test(self, *args):
        try:
            print(args)
        except:
            print("TEST")
