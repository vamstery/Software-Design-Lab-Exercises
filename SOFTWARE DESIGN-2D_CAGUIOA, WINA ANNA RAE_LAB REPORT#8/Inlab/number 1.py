from PyQt5.Widgets import QMainWindow, QApplication, QLabel, QTextEdit, QPushButton
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("number1.ui",self)

        self.show()





app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()