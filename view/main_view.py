import tkinter as tk
from tkinter import filedialog


def butt(*entry):
    print("TeST")


class MainView:
    def __init__(self, x, y):
        self.new_filename = ''
        self.view = tk.Tk(screenName=None, baseName=None, className='Automation', useTk=True)
        self.view.geometry('{}x{}'.format(x, y))

        self.left_frame = new_frame(self.view)
        self.left_frame.pack(side=tk.LEFT, expand=True, padx=10, pady=10)

        self.scrollbar = new_scrollbar(self.left_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.scrollbar_content = tk.Listbox(self.left_frame, yscrollcommand=self.scrollbar.set, width=50, height=15)
        self.scrollbar_content.pack(side=tk.LEFT, fill=tk.X)

        self.right_frame = new_frame(self.view)
        self.right_frame.pack(side=tk.RIGHT, expand=True, padx=10, pady=10)

        self.file_button = new_action_button(self.right_frame, text="Open file", action=self.open_file)
        self.file_button.pack(side=tk.TOP)

        self.play_button = new_action_button(self.right_frame, text="Play", action=butt)
        self.play_button.pack()

        self.new_file_frame = new_frame(self.right_frame)
        self.new_file_frame.pack()

        self.file_entry = new_entry(self.new_file_frame, self.new_filename)
        self.file_entry.pack(side=tk.LEFT)

        self.new_file_button = new_action_button(self.new_file_frame, text="Create", action=butt)
        self.new_file_button.pack(side=tk.RIGHT)

        self.record_button = new_action_button(self.right_frame, text="Record new", action=butt)
        self.record_button.pack(side=tk.BOTTOM)

    def open_file(self) -> None:
        filepath = filedialog.askopenfilename()
        if filepath:
            self.scrollbar_content.delete(0, tk.END)
            index = 0
            nextline = None
            with open(filepath, 'r') as f:
                while nextline != '':
                    nextline = f.readline()
                    self.scrollbar_content.insert(index, nextline)
                    index += 1


def new_action_button(window: tk.Tk, action, text) -> tk.Button:
    button = tk.Button(window, command=action, text=text, activeforeground='blue')
    return button


def new_frame(window) -> tk.Frame:
    frame = tk.Frame(window)
    return frame


def new_entry(window, text) -> tk.Entry:
    entry = tk.Entry(window, textvariable=text)
    return entry


def new_scrollbar(window) -> tk.Scrollbar:
    scrollbar = tk.Scrollbar(window)
    return scrollbar
