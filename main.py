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

import os
from models.queue import Queue
from models.process import Process

print("Aqui ira el menu")


n = str(input("Numero de Procesos a Introducir: "))
while (n.isdigit() == False or int(n) < 1):
    os.system("clear" | "cls")
    print("[ERROR] introduce un numero")
    n = str(input("Numero de Procesos a Introducir: "))
n = int(n)