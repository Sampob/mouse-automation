from controller.actions.action_interface import ActionInterface
import controller.file_interpeting.file_interpreter


class ExecuteAction(ActionInterface):

    def __init__(self):
        super().__init__('EXECUTE')

    def execute_action(self, values) -> bool:
        """
        Start execution of another script
        :param values: script path and name
        :return: bool to continue or stop
        """
        ex = controller.file_interpeting.file_interpreter.FileController()
        ex.set_filename(values[0])

        try:
            times = int(values[1])
        except IndexError:
            times = 1

        for i in range(times):
            ex.readfile()

        return True
