from controller.file_interpeting.file_interpreter import FileController
from view.main_view import MainView

if __name__ == '__main__':
    fc = FileController()

    mv = MainView(600, 250)

    window = mv.view
    window.mainloop()
