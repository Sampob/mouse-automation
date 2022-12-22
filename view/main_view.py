import tkinter as tk
from tkinter import filedialog

"""
OLD WAY OF DOING
SAFE TO DELETE
ONLY FOR DOCUMENTATION PURPOSES
"""

def butt(*entry):
    print("TeST")


class MainView:
    def __init__(self, x, y):
        self.new_filename = ''
        self.view = tk.Tk(screenName=None, baseName=None, className='Automation', useTk=True)
        self.view.geometry('{}x{}'.format(x, y))
        self.automation_view()

    def automation_view(self):
        left_frame = new_frame(self.view)
        left_frame.pack(side=tk.LEFT, expand=True, padx=10, pady=10)

        scrollbar = new_scrollbar(left_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        scrollbar_content = tk.Listbox(left_frame, yscrollcommand=scrollbar.set, width=50, height=15)
        scrollbar_content.pack(side=tk.LEFT, fill=tk.Y)

        right_frame = new_frame(self.view)
        right_frame.pack(side=tk.RIGHT, expand=True, padx=10, pady=10)

        file_button = new_action_button(right_frame, text="Open file",
                                        action=lambda: self.open_file(scrollbar_content))
        file_button.grid(row=0, column=0)
        # file_button.pack(side=tk.TOP)

        play_button = new_action_button(right_frame, text="Play", action=butt)
        play_button.grid(row=1, column=0)
        # play_button.pack()

        new_file_frame = new_frame(right_frame)
        new_file_frame.grid(row=2, column=0)
        # new_file_frame.pack()

        file_entry = new_entry(new_file_frame, self.new_filename)
        file_entry.pack(side=tk.LEFT)

        new_file_button = new_action_button(new_file_frame, text="Create", action=butt)
        new_file_button.pack(side=tk.RIGHT)

        record_button = new_action_button(right_frame, text="Record new", action=butt)
        record_button.grid(row=3, column=0)
        # record_button.pack(side=tk.BOTTOM)

    def open_file(self, element) -> None:
        filepath = filedialog.askopenfilename()
        if filepath:
            element.delete(0, tk.END)
            index = 0
            nextline = None
            with open(filepath, 'r') as f:
                while nextline != '':
                    nextline = f.readline()
                    element.insert(index, nextline)
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
