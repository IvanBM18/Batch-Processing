#Validar Entradas
#Decidir como se imprimira el proceso actual(proces toString())
#SubMenu de opciones para introducir un proceso nuevo
#SubMenu muestra cantidad de procesos restantes por ingresar
#Opciones del SubMenu:
# 1-Cambiar Nombre del programador
# 2-Ingresar nuevo proceso
# 0-Salir del Programa
#Añadir los procesos a la cola
#Pantalla de ejecución de los lotes
#Color blanco del textBox_numero2
# import os
# from models.queue import Queue
# from models.process import Process
#si te da error, instala pyside2 para checar si esta es pip show pyside2
from PySide2.QtWidgets import QApplication

from controllers.main_window import MainForm 
import sys

if __name__ == '__main__':
    # Aplicación de Qt
    app = QApplication()
    # Se crea un botón con la palabra Hola
    window=MainForm()
    # Se hace visible el botón
    window.show()
    # Qt loop
    sys.exit(app.exec_())



# print("Aqui ira el menu")


# n = str(input("Numero de Procesos a Introducir: "))
# while (n.isdigit() == False or int(n) < 1):
#     os.system("clear" | "cls")
#     print("[ERROR] introduce un numero")
#     n = str(input("Numero de Procesos a Introducir: "))
# n = int(n)