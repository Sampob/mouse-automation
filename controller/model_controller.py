from model.file_interpeting.file_interpreter import FileController


class ModelController:
    def __init__(self, file_controller: FileController):
        self.fc = file_controller

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

    def test(self, *args):
        try:
            print(args)
        except:
            print("TEST")
