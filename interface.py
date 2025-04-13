import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QLabel, QWidget, QLineEdit, QPushButton

class Interface(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Alarme")
        self.setGeometry(100,100,600,400)

        self.caixa_input = QLineEdit(self)
        self.caixa_input.move(180,50)

        self.set_alarm = QPushButton("Set Alarm", self)
        self.set_alarm.move(50,50)
        self.set_alarm.resize(100, 40)

        self.parar = QPushButton("Parar", self)
        self.parar.move(50,100)
        self.set_alarm.resize(100, 40)


def Janela():
    app = QApplication(sys.argv)
    janela = Interface()
    janela.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    Janela()