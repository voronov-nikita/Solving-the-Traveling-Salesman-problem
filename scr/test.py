import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QWhatsThis, QVBoxLayout


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Dialog with Help')

        label = QLabel("This is a dialog with help.")
        self.setWhatsThis("This is the help text for the dialog.")

        button = QPushButton("Help")
        button.clicked.connect(self.showHelp)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        self.setLayout(layout)

    def showHelp(self):
        QWhatsThis.enterWhatsThisMode()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())
