import sys
from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit, QPushButton

class Interface(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Alarnme")

        self.caixa_input = QLineEdit
