from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QApplication, QDialog,\
QLabel, QWhatsThis
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QFile
import pyautogui
import sys

from main import FindMinWay


class ErrorValueDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.window_name = "Error"
        self.window_size = (500, 200)
        self.window_icon = "../images/icon/IconApp.ico"

        self.InitWindow()
        self.InitText()

    def InitWindow(self):
        # Window params
        self.setWindowIcon(QIcon(self.window_icon))
        self.setWindowTitle(self.window_name)
        x, y = pyautogui.size()
        self.setGeometry((x-self.window_size[0])//2, (y-self.window_size[1])//2, *self.window_size)
        self.setFixedSize(self.width(), self.height())
        self.setWhatsThis("This is the help text for the dialog.")

    def InitText(self):

        warning_text = QLabel(self)
        warning_text.setText("Внимание!\nБыли введены неправильные данные в одну из строк.\nПроверьте их и попробуйте снова.")
        warning_text.resize(*self.window_size)
        warning_text.setStyleSheet("""
            background: rgb(47, 90, 109);
            color: rgb(255, 224, 41);
            border: 1px solid rgb(255, 224, 41);
            text-align: center;
            font-weight: bold;
            font-family: Times New Roman;
            font-size: 20px;
        """)


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window_name = "Main"
        self.window_icon = "../images/icon/IconApp.ico"
        self.window_size = (400, 400)
        self.precent_height = 0.15
        self.precent_height_button = 0.25

        self.InitGui()

    def InitGui(self):
        # Window params
        self.setWindowIcon(QIcon(self.window_icon))
        self.setWindowTitle(self.window_name)
        x, y = pyautogui.size()
        self.setGeometry((x-self.window_size[0])//2, (y-self.window_size[1])//2, *self.window_size)
        self.setFixedSize(self.width(), self.height())


        # Interface params
        self.line_count_point = QLineEdit(self)
        self.line_count_point.setPlaceholderText("The Count of Point")
        self.line_count_point.resize(int(self.window_size[0]), int(self.window_size[1]*self.precent_height))
        self.line_count_point.move(0, int(self.window_size[1]*self.precent_height) * 0)
        self.line_count_point.setStyleSheet("""
            background: rgb(40, 40, 40);
            color: rgb(0, 255, 175);
            border: 1px solid rgb(0, 200, 120);
        """)

        self.line_round_point = QLineEdit(self)
        self.line_round_point.setPlaceholderText("The Round")
        self.line_round_point.resize(int(self.window_size[0]), int(self.window_size[1]*self.precent_height))
        self.line_round_point.move(0, int(self.window_size[1]*self.precent_height) * 1)
        self.line_round_point.setStyleSheet("""
            background: rgb(40, 40, 40);
            color: rgb(0, 255, 175);
            border: 1px solid rgb(0, 200, 120);
        """)

        self.line_min_position = QLineEdit(self)
        self.line_min_position.setPlaceholderText("The Min Position")
        self.line_min_position.resize(int(self.window_size[0]), int(self.window_size[1]*self.precent_height))
        self.line_min_position.move(0, int(self.window_size[1]*self.precent_height) * 2)

        self.line_max_position = QLineEdit(self)
        self.line_max_position.setPlaceholderText("The Max Position")
        self.line_max_position.resize(int(self.window_size[0]), int(self.window_size[1]*self.precent_height))
        self.line_max_position.move(0, int(self.window_size[1]*self.precent_height) * 3)

        self.line_start_point = QLineEdit(self)
        self.line_start_point.setPlaceholderText("The index Start Point")
        self.line_start_point.resize(int(self.window_size[0]), int(self.window_size[1]*self.precent_height))
        self.line_start_point.move(0, int(self.window_size[1]*self.precent_height) * 4)


        self.button_start = QPushButton(self)
        self.button_start.setText("Start")
        self.button_start.resize(int(self.window_size[0]), int(self.window_size[1]*self.precent_height_button))
        self.button_start.move(0, self.window_size[1]-int(self.window_size[1]*self.precent_height_button))
        self.button_start.clicked.connect(self.start_calculate)


    def start_calculate(self):
        try:
            count_point = int(self.line_count_point.text())
            round_value = int(self.line_round_point.text())
            min_position = int(self.line_min_position.text())
            max_position = int(self.line_max_position.text())
            start_point = int(self.line_start_point.text())

            minway = FindMinWay()
            list_point = minway.create_list_point(count_point, round_value, min_position, max_position)
            result_function = minway.finally_variant(list_point, start_point)
            new_list = result_function
            minway.show_way(new_list, start_point=start_point)

        except ValueError:
            dialog = ErrorValueDialog()
            dialog.exec_()



if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec_())
