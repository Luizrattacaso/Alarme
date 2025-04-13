from email.mime import application
import sys
from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit, QPushButton

class Interface(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Alarnme")

        self.caixa_input = QLineEdit
        self.set_alarm = QPushButton("Set Alarm")
        self.parar = QPushButton("Set Alarm")


if __name__ == "__name__":
    app = application(sys.argv)