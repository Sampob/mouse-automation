from model.file_interpeting import FileController
from view.pygubu_view import GubuView

if __name__ == '__main__':
    fc = FileController()

    gubu = GubuView()
    gubu.run()
