from controller.model_controller import ModelController
from view.pygubu_view import GubuView

if __name__ == '__main__':

    mc = ModelController()

    gubu = GubuView(mc)
    gubu.run()
