#Adaptar generación de procesos a la nueva información
# tecla = ord(getch())
#e = 101
# W = 119
# P = 112
# c = 99
from concurrent.futures import process
from msvcrt import getch, kbhit
import random
from typing import Any
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from PySide6.QtCore import QTimer

from view.mainwindow import MainWindow
from models.queue import Queue
from models.process import Process
from models.batch import Batch


class MainForm(QMainWindow, MainWindow):
    #Atributtes
    totalProcess : int = 0
    queue = Queue() #Cola de Lotes
    batch = Batch() #Batch Actual
    
    counting = False #Bandera para iniciar el proceso de ejecucion
    timer : Any  #Timer que se ejecuta cada segundo para actualizar el contador global
    
    #Variables to be used during process Execution
    actualProcess : Process
    batchCounter = 0 #Contador de batches para pasar a la siguiente tabla
    timeCounter = 0 #Contador de Tiempo Global
    elapsedTime = 0 #Contador de Tiempo de Proceso
    remainingTime = 0 #Tiempo restante del proceso
    counter = 0 #Contador de Lotes para textbox restantes
    indxB = 0 #Indice del batch
    batchInTable = False
    indxP = 0 #Indice del proceso en el batch en ejecución, en creación indice actual
    
    #Constructor
    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTimer)
        self.timer.start(1000)
        self.setupUi(self)
        self.pushButton_Agregar.clicked.connect(self.setTotalProcess)
        self.pushButton_ejecturar.clicked.connect(self.processBatches)
        self.pushButton_ejecturar.setEnabled(False)
        
    
    #Setters
    def setTotalProcess(self):
        validateEntry = self.textBox_NumProcess.text()
        if (str(validateEntry).isdigit() == False and validateEntry != "" and validateEntry > 0):
            print("[ERROR] introduce un numero")
            msgBox = QMessageBox()
            msgBox.setText("Introduce un numero")
            msgBox.setWindowTitle("ERROR en ID")
            msgBox.exec_()
            self.textBox_NumProcess.setText("")
        else:
            if(self.queue.getLength() != 0):
                self.queue = Queue()
                self.batch = Batch()
            self.totalProcess = int(validateEntry)
            self.pushButton_ejecturar.setEnabled(True)
    
    #Processing Methods
    def updateTimer(self):
        first = False
        # Eliminar repeticion de set text timeCounter
        if(self.counting == True):
            if ((self.queue.getLength() == 0) and (self.batch.getRemainingProcess() == 0) and (self.remainingTime == 0)): #Fin del Procesamiento
                self.textBox_restantes.setText(str(0))
                self.tablaProcesos.clearContents()
                self.counting = False
                return
            if(self.batchInTable == False): #Caso 0
                self.batch = self.queue.dequeue() #Batch de 3 Procesos
                self.insertBatch(self.batch.getProcessList())
                self.elapsedTime = 0
                self.actualProcess = self.batch.getTopProcess() #Proceso Actual
                self.remainingTime = self.actualProcess.getTime() #Tiempo restante del proceso
                self.textBox_operacion.setText(self.actualProcess.getFullOperation())
                self.textBox_tiempo_transcurrido.setText(str(self.elapsedTime))
                self.textBox_tiempo_restante.setText(str(self.remainingTime))
                self.textBox_Id_proceso.setText(str(self.actualProcess.getID()))
                self.textBox_contadorGlobal.setText(str(self.timeCounter))
                self.batchInTable = True
                first = True
            if(self.remainingTime == 0): #Cambio de Proceso
                self.insertRow(self.actualProcess,self.batchCounter) 
                self.tablaProcesos.removeRow(0)
                self.batch.removeProcess()
                if(self.batch.getRemainingProcess() != 0): #Si quedan aun procesos
                    self.elapsedTime = 0 #Tiempo transcurrido del proceso
                    self.actualProcess = self.batch.getTopProcess() #Obtenemos un nuevo proceso
                    self.remainingTime = self.actualProcess.getTime() #Tiempo restante del proceso
                    self.textBox_operacion.setText(self.actualProcess.getFullOperation())
                    self.textBox_tiempo_transcurrido.setText(str(self.elapsedTime))
                    self.textBox_tiempo_restante.setText(str(self.remainingTime))
                    self.textBox_Id_proceso.setText(str(self.actualProcess.getID()))
            if(self.batch.getRemainingProcess() == 0): #Fin del Batch
                self.tablaProcesos.clearContents()
                if(self.queue.getLength() != 0): #Si quedan aun batches
                    self.batch = self.queue.dequeue()       
                    self.insertBatch(self.batch.getProcessList())
                self.counter -=1
                self.textBox_restantes.setText(str(self.counter))
                self.batchCounter += 1
            elif(not first): #Continuamos con el proceso
                self.timeCounter += 1
                self.elapsedTime += 1
                self.remainingTime -= 1
                self.textBox_tiempo_transcurrido.setText(str(self.elapsedTime))
                self.textBox_tiempo_restante.setText(str(self.remainingTime))
                self.textBox_contadorGlobal.setText(str(self.timeCounter))
    
    #Checar esto no sirve al 100
    def processBatches(self):
        if(self.totalProcess != 0):
            self.counter = self.totalProcess//3 #Contador de Lotes
            if(self.totalProcess%3 != 0):
                self.counter += 1
            self.timeCounter = 0 #Contador de Tiempo Global
            self.elapsedTime = 0 #Contador de Tiempo de Proceso
            self.remainingTime = 0 #Tiempo restante del proceso
            self.counter -= 1
            self.textBox_restantes.setText(str(self.counter))
            self.generateProcess()
            self.counting = True

    #Generate new Process
    def newProcess(self) -> Process:
        if(self.totalProcess != 0):
            operation = ""
            procesNum = random.randint(0,5)
            if(procesNum == 0):
                operation = "+"
            elif (procesNum == 1):
                operation = "-"
            elif (procesNum == 2):
                operation = "*"
            elif(procesNum == 3):
                operation = "/"
            elif (procesNum == 4):
                operation = "%"
            elif(procesNum == 5):
                operation = "^"	
            newProcess = Process((random.randint(1,100)),(random.randint(1,100)),operation,(random.randint(1,5)),self.indxP)
            self.indxP +=1
        return newProcess
    
    #Generate Process till end
    def generateProcess(self):
        if(self.totalProcess > 0):
            cont = 0
            auxCont = 0
            newProcess : Process
            while(cont < self.totalProcess):
                newProcess = self.newProcess()
                self.batch.addProcess(newProcess)
                cont += 1
                auxCont += 1
                if(auxCont == 3):
                    self.queue.enqueue(self.batch)
                    self.batch = Batch()
                    auxCont = 0
            if(auxCont != 0):
                self.queue.enqueue(self.batch)
            self.indxP = 0
    
    #Visual Methods
    def insertBatch(self,batch:list):
        self.tablaProcesos.clearContents()
        aux : Process
        for i in range(len(batch)):
            n = self.tablaProcesos.rowCount()
            aux = batch[i]
            self.tablaProcesos.insertRow(n)
            self.tablaProcesos.setItem(n,0,QTableWidgetItem(aux.getID()))
            self.tablaProcesos.setItem(n,1,QTableWidgetItem(str(aux.getTime())))
            self.tablaProcesos.setItem(n,2,QTableWidgetItem(str(aux.getElapsedTime())))
    
    def insertRow(self,row:Process,batch:int):
        n = self.tablaPTerminados.rowCount()
        self.tablaPTerminados.insertRow(n)
        self.tablaPTerminados.setItem(n,0,QTableWidgetItem(str(self.batchCounter)))
        self.tablaPTerminados.setItem(n,1,QTableWidgetItem(str(row.getID())))
        self.tablaPTerminados.setItem(n,2,QTableWidgetItem(row.getFullOperation()))
        self.tablaPTerminados.setItem(n,3,QTableWidgetItem(str(row.getResult())))