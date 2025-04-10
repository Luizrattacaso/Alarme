import time
import datetime
from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit, QPushButton

def set_alarm(alarm_time):
    print(f"Alarme posto para {alarm_time}")
    is_running = True

    while is_running:
        hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
        print(hora_atual)

        if alarm_time == hora_atual:
            print("Hora de acordar!")
            is_running = False

        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Insira o alarme(Hh:Mm:Ss): ")
    set_alarm(alarm_time)