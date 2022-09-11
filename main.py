#Añadir los procesos a la cola
#Pantalla de ejecución de los lotes
from PySide6.QtWidgets import QApplication

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
    sys.exit(app.exec()) #use exec?



# print("Aqui ira el menu")


# n = str(input("Numero de Procesos a Introducir: "))
# while (n.isdigit() == False or int(n) < 1):
#     os.system("clear" | "cls")
#     print("[ERROR] introduce un numero")
#     n = str(input("Numero de Procesos a Introducir: "))
# n = int(n)