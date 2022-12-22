from controller.file_interpeting.file_interpreter import FileController
from view.main_view import MainView
from view.pygubu_view import GubuView

if __name__ == '__main__':
    fc = FileController()

    gubu = GubuView()
    gubu.run()
