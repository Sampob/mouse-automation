import pathlib
import tkinter as tk
from threading import Thread
from tkinter import filedialog

import pygubu

from controller.model_controller import ModelController

FILE_PATH = pathlib.Path(__file__).parent
PROJECT_UI = FILE_PATH / "pygubu/mainview.ui"


class GubuView:
    def __init__(self, master=None, model: ModelController = None):
        self.model = model
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(FILE_PATH)

        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('mainwindow', master)

        builder.connect_callbacks(self)

    def browse_command(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            self.model.set_script(filepath)
            self.builder.get_object('filenamelable').config(text=filepath)
            self.set_filelist(self.read_file_lines(filepath=filepath))

    def read_file_lines(self, filepath):
        with open(filepath, 'r') as f:
            return f.readlines()

    def set_filelist(self, text: 'list', index: int = 0):
        element = self.builder.get_object('filelist')
        element.delete(0, tk.END)
        for i in range(len(text)):
            element.insert(i, text[i])
        self.set_selected_item(index)

    def set_selected_item(self, index):
        self.builder.get_object('filelist').select_set(index)

    def indef_click(self):
        state = tk.NORMAL
        if self.builder.tkvariables['indefvar'].get():
            state = tk.DISABLED
        self.builder.get_object('timesspinbox').config(state=state)

    def execute_button(self):
        execute_thread = Thread(target=self.model.execute_script, args=(
            self.builder.tkvariables['indefvar'].get(), int(self.builder.get_object('timesspinbox').get()),))
        execute_thread.start()

    def record_button(self):
        self.model.record("data/" + self.builder.tkvariables['filenameentry'].get())

    def test(self, *args):
        self.set_filelist()

    def run(self):
        self.mainwindow.mainloop()
