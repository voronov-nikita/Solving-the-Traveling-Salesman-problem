from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QApplication, QDialog,\
QLabel
from PyQt5.QtGui import QIcon
from threading import Thread
import pyautogui
import sys

from main import FindMinWay

class GetData(QDialog):
    def __init__(self, time, len_way):
        super().__init__()
        self.window_name = "Data"
        self.window_size = (450, 200)
        self.window_icon = "../images/icon/IconApp.ico"

        self.time = time
        self.len_way = len_way
        
        self.InitWindow()
        self.InitInterface()
    
    def InitWindow(self):
        self.setWindowTitle(self.window_name)
        x, y = pyautogui.size()
        self.setGeometry((x-self.window_size[0])//2, (y-self.window_size[1])//2, self.window_size[0], self.window_size[1])
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon(self.window_icon))

    def InitInterface(self):
        self.data_text = QLabel(self)
        self.data_text.setText(f"TIME: {self.time}sec\nLEN ALL WAY: {self.len_way} units\nSTART POINT: RED")
        self.data_text.resize(*self.window_size)
        self.data_text.setStyleSheet("""
            background: rgb(40, 40, 40);
            color: rgb(0, 255, 175);
            border: 1px solid rgb(0, 100, 20);
            text-align: center;
            font-weight: bold;
            font-size: 26px;
        """)
        

class ErrorValueDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.window_name = "Error"
        self.window_size = (502, 202)
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
        warning_text.setText("\t\tВнимание! \nБыли введены неправильные данные в одну из строк.\n\tПроверьте их и попробуйте снова.")
        warning_text.resize(*self.window_size)
        warning_text.setStyleSheet("""
            background: rgb(40, 40, 40);
            color: rgb(0, 255, 175);
            border: 1px solid rgb(0, 100, 20);
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
        self.precent_height = 0.125
        self.precent_height_label = 0.1
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

        self.label = QLabel(self)
        self.label.setText("    Введите данные, согласно названиям на линиях.")
        self.label.resize(self.window_size[0], int(self.window_size[1]*self.precent_height))
        self.label.move(0, int(self.window_size[1]*self.precent_height_label) * 0)
        self.label.setStyleSheet("""
            background: rgb(40, 40, 40);
            color: rgb(0, 255, 175);
            border: 1px solid rgb(0, 100, 20);
            text-align: center;
        """)

        self.line_count_point = QLineEdit(self)
        self.line_count_point.setPlaceholderText("The Count of Point")
        self.line_count_point.resize(int(self.window_size[0]), int(self.window_size[1]*self.precent_height))
        self.line_count_point.move(0, int(self.window_size[1]*(self.precent_height)) * 1)
        self.line_count_point.setStyleSheet("""
            background: rgb(40, 40, 40);
            color: rgb(0, 255, 175);
            border: 1px solid rgb(0, 100, 20);
        """)

        self.line_round_point = QLineEdit(self)
        self.line_round_point.setPlaceholderText("The Round")
        self.line_round_point.resize(int(self.window_size[0]), int(self.window_size[1]*self.precent_height))
        self.line_round_point.move(0, int(self.window_size[1]*self.precent_height) * 2)
        self.line_round_point.setStyleSheet("""
            background: rgb(40, 40, 40);
            color: rgb(0, 255, 175);
            border: 1px solid rgb(0, 100, 20);
        """)

        self.line_min_position = QLineEdit(self)
        self.line_min_position.setPlaceholderText("The Min Position")
        self.line_min_position.resize(int(self.window_size[0]), int(self.window_size[1]*self.precent_height))
        self.line_min_position.move(0, int(self.window_size[1]*self.precent_height) * 3)
        self.line_min_position.setStyleSheet("""
            background: rgb(40, 40, 40);
            color: rgb(0, 255, 175);
            border: 1px solid rgb(0, 100, 20);
        """)

        self.line_max_position = QLineEdit(self)
        self.line_max_position.setPlaceholderText("The Max Position")
        self.line_max_position.resize(int(self.window_size[0]), int(self.window_size[1]*self.precent_height))
        self.line_max_position.move(0, int(self.window_size[1]*self.precent_height) * 4)
        self.line_max_position.setStyleSheet("""
            background: rgb(40, 40, 40);
            color: rgb(0, 255, 175);
            border: 1px solid rgb(0, 100, 20);
        """)

        self.line_start_point = QLineEdit(self)
        self.line_start_point.setPlaceholderText("The index Start Point")
        self.line_start_point.resize(int(self.window_size[0]), int(self.window_size[1]*self.precent_height))
        self.line_start_point.move(0, int(self.window_size[1]*self.precent_height) * 5)
        self.line_start_point.setStyleSheet("""
            background: rgb(40, 40, 40);
            color: rgb(0, 255, 175);
            border: 1px solid rgb(0, 100, 20);
        """)


        self.button_start = QPushButton(self)
        self.button_start.setText("Start")
        self.button_start.resize(int(self.window_size[0]), int(self.window_size[1]*self.precent_height_button))
        self.button_start.move(0, self.window_size[1]-int(self.window_size[1]*self.precent_height_button))
        self.button_start.clicked.connect(self.start_calculate)
        self.button_start.setStyleSheet("""
        background: rgb(20, 20, 20);
        color: rgb(52, 189, 176);
        border: 1px solid rgb(0, 200, 120);
        font-weight: bold;
        """)


    def open_data_window(self, timer, lenway):
        data_window = GetData(timer, lenway)
        data_window.exec_()

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

            self.open_data_window(timer=minway.get_execution_time(), lenway=new_list[1])

        except ValueError:
            dialog = ErrorValueDialog()
            self.line_count_point.clear()
            self.line_round_point.clear()
            self.line_max_position.clear()
            self.line_min_position.clear()
            self.line_start_point.clear()
            dialog.exec_()



if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec_())
