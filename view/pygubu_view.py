import pathlib
import pygubu

FILE_PATH = pathlib.Path(__file__).parent
PROJECT_UI = FILE_PATH / "pygubu/mainview.ui"


class GubuView:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(FILE_PATH)

        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('mainwindow', master)

        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()
