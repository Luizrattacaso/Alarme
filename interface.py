import sys
import time
import datetime
from PyQt5.QtWidgets import QMainWindow,QApplication, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal

class AlarmeThread(QThread):
    alarme_disparado = pyqtSignal()

    def __init__(self, tempo_alarme):
        super().__init__()
        self.tempo_alarme = tempo_alarme
        self.running = True

    def run(self):
        print(f"Alarme posto para {self.tempo_alarme}")
        self.running = True

        while self.running:
            hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
            print(hora_atual)
            if self.tempo_alarme == hora_atual:
               self.alarme_disparado.emit()
               self.running = False
            time.sleep(1)

    def parar(self):
        self.running = False
     
class Interface(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Alarme")
        self.setGeometry(100,100,600,400)

        self.caixa_input = QLineEdit(self)
        self.caixa_input.move(180,50)
        self.caixa_input.resize(120,30)

        self.set_alarm = QPushButton("Set Alarm", self)
        self.set_alarm.move(50,50)
        self.set_alarm.resize(100, 40)
        self.set_alarm.clicked.connect(self.iniciar_alarme)

        self.parar = QPushButton("Parar", self)
        self.parar.move(50,100)
        self.parar.resize(100, 40)
        self.parar.clicked.connect(self.parar_alarme)

        self.alarme_thread = None

    def iniciar_alarme(self):
        tempo = self.caixa_input.text()
        try:
            datetime.datetime.now().strftime("%H:%M:%S")
            self.alarme_thread = AlarmeThread(tempo)
            self.alarme_thread.alarme_disparado.connect(self.exibir_mensagem)
            self.alarme_thread.start()
            print("Alarme iniciado")
        except ValueError:
            QMessageBox.warning(self,"Erro", "Formato inválido. Use Hora:Min:Seg.")

    def parar_alarme(self):
        if self.alarme_thread:
            self.alarme_thread.parar()
            self.alarme_thread = None
            print("Alarme parado")

    def exibir_mensagem(self):
        QMessageBox.information(self,"Alarme","Hora de acordar!")

def Janela():
    app = QApplication(sys.argv)
    janela = Interface()
    janela.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    Janela()