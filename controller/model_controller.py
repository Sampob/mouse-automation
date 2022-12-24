from model.file_interpeting.file_interpreter import FileController


class ModelController:
    def __init__(self):
        self.fc = FileController()

    def set_script(self, script):
        self.fc.set_filename(script)

    def execute_script(self, loop: bool = False, times: int = None):
        if loop:
            while True:
                self.fc.readfile()
        elif times and times > 0:
            for i in range(times):
                self.fc.readfile()
        else:
            print("NEG")

    def record(self, filename):
        if filename != 'data/':
            print(filename)

    def get_file_controller(self):
        return self.fc

    def test(self, *args):
        try:
            print(args)
        except:
            print("TEST")
