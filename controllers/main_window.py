#Validaciones
#Division por 0
import time
from typing import Any
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from PySide6.QtCore import QTimer

from view.mainwindow import MainWindow
from models.queue import Queue
from models.process import Process


class MainForm(QMainWindow, MainWindow):
    #Atributtes
    totalProcess : int = 0
    name : str = ""
    operation : str = "+"
    queue = Queue()
    counting = False #Bandera para iniciar el proceso de ejecucion
    timer : Any  #Timer que se ejecuta cada segundo para actualizar el contador global
    
    batch = [] #Lista de procesos a ejecturar
    batchCounter = 0 #Contador de batches
    timeCounter = 0 #Contador de Tiempo Global
    elapsedTime = 0 #Contador de Tiempo de Proceso
    remainingTime = 0 #Tiempo restante del proceso
    counter = 0 #Contador de Lotes
    indxB = 0 #Indice del batch
    batchInTable = False
    indxP = 0 #Indice del proceso en el batch
    
    #Constructor
    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTimer)
        self.timer.start(1000)
        self.setupUi(self)
        #self.pushButton_aceptProcess.clicked.connect(self.setTotalProcess)
        self.pushButton_Agregar.clicked.connect(self.newProcess)
        self.textBox_Nombre.textChanged.connect(self.setName)
        self.textBox_numero1.textChanged.connect(self.setOperationFirst)
        self.textBox_numero2.textChanged.connect(self.setOperationSecond)
        self.textBox_tiempo.textChanged.connect(self.setTime)
        self.textBox_Id.textChanged.connect(self.setID)
        self.pushButton_ejecturar.clicked.connect(self.processBatches)
        self.pushButton_ejecturar.setEnabled(False)
        
    
    #Setters
    def setName(self):
        self.name = self.textBox_Nombre.text()
        
    def setOperationFirst(self):
        validateEntry = self.textBox_numero1.text()
        if (str(validateEntry).isdigit() == False and validateEntry != ""):
            print("[ERROR] introduce un numero")
            msgBox = QMessageBox()
            msgBox.setText("Introduce un numero mayor a 0")
            msgBox.setWindowTitle("ERROR en valores de operación")
            msgBox.exec_()
            self.textBox_numero1.setText("")
            
    def setOperationSecond(self):
        validateEntry = self.textBox_numero2.text()
        if (str(validateEntry).isdigit() == False and validateEntry != ""):
            print("[ERROR] introduce un numero")
            msgBox = QMessageBox()
            msgBox.setText("Introduce un numero mayor a 0")
            msgBox.setWindowTitle("ERROR en valores de Operación")
            msgBox.exec_()
            self.textBox_numero2.setText("")
    
    def setTime(self):
        validateEntry = self.textBox_tiempo.text()
        if ((str(validateEntry).isdigit() == False or int(validateEntry) < 1) and validateEntry != ""):
            print("[ERROR] introduce un numero")
            msgBox = QMessageBox()
            msgBox.setText("Introduce un numero mayor a 0")
            msgBox.setWindowTitle("ERROR en Tiempo")
            msgBox.exec_()
            self.textBox_tiempo.setText("")
    
    def setID(self):
        validateEntry = self.textBox_Id.text()
        if (str(validateEntry).isdigit() == False and validateEntry != ""):
            print("[ERROR] introduce un numero")
            msgBox = QMessageBox()
            msgBox.setText("Introduce un numero")
            msgBox.setWindowTitle("ERROR en ID")
            msgBox.exec_()
            self.textBox_Id.setText("")
    
    #Methods
    def newProcess(self):
        if(self.name != ""):
            operation  = self.comboBoxOperaciones.currentText()
            if(operation == "/"):
                if(int(self.textBox_numero2.text()) == 0):
                    msgBox = QMessageBox()
                    msgBox.setText("Introduce un numero mayor a 0")
                    msgBox.setWindowTitle("ERROR en valores de operación")
                    msgBox.exec_()
                    self.textBox_numero2.setText("")
            self.operation = operation
            aux = Process(self.name,int(self.textBox_numero1.text()),int(self.textBox_numero2.text()),operation,int(self.textBox_tiempo.text()),self.textBox_Id.text())
            self.queue.enqueue(aux)
            self.totalProcess += 1
            self.textBox_Id.setText(str(int(self.textBox_Id.text())+1))
            self.pushButton_ejecturar.setEnabled(True)
        self.textBox_numero1.setText("")
        self.textBox_numero2.setText("")
        self.textBox_tiempo.setText("")
    
    def updateTimer(self):
        if(self.counting == True):
            #self.textBox_contadorGlobal.setText(str(int(self.textBox_contadorGlobal.text())+1))
            if ((self.indxP == 3 and self.indxB +3 >= self.totalProcess) or self.counter == -1): #Fin del Procesamiento
                self.textBox_restantes.setText(str(0))
                self.tablaProcesos.clearContents()
                self.counting = False
                return
            if(self.batchInTable == False): #Caso 0
                self.batch = self.queue.getBatch(self.indxB) #Batch de 3 Procesos
                self.insertBatch(self.batch)
                self.elapsedTime = 0
                self.remainingTime = self.batch[self.indxP].getTime() #Tiempo restante del proceso
                self.textBox_Nombre_proceso.setText(self.batch[self.indxP].getName())
                self.textBox_operacion.setText(self.batch[self.indxP].getFullOperation())
                self.textBox_tiempo_transcurrido.setText(str(self.elapsedTime))
                self.textBox_tiempo_restante.setText(str(self.remainingTime))
                self.textBox_Id_proceso.setText(str(self.batch[self.indxP].getID()))
                self.textBox_contadorGlobal.setText(str(self.timeCounter))
                self.batchInTable = True
            if(self.remainingTime == 0): #Cambio de Proceso
                self.insertRow(self.queue.dequeue(),self.batchCounter)
                self.tablaProcesos.removeRow(0)
                self.indxP += 1
                if(self.indxP < len(self.batch)): #Cambio de Batch
                    self.elapsedTime = 0 #Tiempo transcurrido del proceso
                    self.remainingTime = self.batch[self.indxP].getTime() #Tiempo restante del proceso
                    self.textBox_Nombre_proceso.setText(self.batch[self.indxP].getName())
                    self.textBox_operacion.setText(self.batch[self.indxP].getFullOperation())
                    self.textBox_tiempo_transcurrido.setText(str(self.elapsedTime))
                    self.textBox_tiempo_restante.setText(str(self.remainingTime))
                    self.textBox_Id_proceso.setText(str(self.batch[self.indxP].getID()))
                    self.textBox_contadorGlobal.setText(str(self.timeCounter))
            if((self.indxP == 3 and self.indxB +3 < self.totalProcess) or self.indxP == len(self.batch)): #Fin del Batch
                self.indxB += 3
                self.indxP = 0
                self.tablaProcesos.clearContents()
                self.batch = self.queue.getBatch(self.indxB)
                self.insertBatch(self.batch)
                self.counter -=1
                self.textBox_restantes.setText(str(self.counter))
                self.batchCounter += 1
            else: #Continuamos con el proceso
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
            self.batch = []
            self.counter -= 1
            self.textBox_restantes.setText(str(self.counter))
            self.counting = True
            # for i in range(0,self.totalProcess,3):
            #     self.textBox_restantes.setText(str(counter-1))
            #     if(i < self.totalProcess): #Dentro del Rango de 3 procesos por lote
            #         self.batch = self.queue.getBatch(i) #Batch de 3 Procesos
            #         self.insertBatch(self.batch) #<-
            #         for j in range(len(self.batch)): #3 Procesos por lote
                        
            #             self.remainingTime = self.batch[j].getTime() #Tiempo restante del proceso
            #             self.textBox_Nombre_proceso.setText(self.batch[j].getName())
            #             self.textBox_operacion.setText(self.batch[j].getFullOperation())
            #             self.textBox_tiempo_transcurrido.setText(str(self.elapsedTime))
            #             self.textBox_tiempo_restante.setText(str(self.remainingTime))
            #             self.textBox_Id_proceso.setText(str(self.batch[j].getID()))
            #             self.textBox_contadorGlobal.setText(str(self.timeCounter))
            #             while(self.remainingTime > 0): #Proceso en Ejecución
            #                 time.sleep(1)
            #                 self.timeCounter += 1
            #                 self.elapsedTime += 1
            #                 self.remainingTime -= 1
            #                 self.textBox_tiempo_transcurrido.setText(str(self.elapsedTime))
            #                 self.textBox_tiempo_restante.setText(str(self.remainingTime))
            #                 self.textBox_contadorGlobal.setText(str(self.timeCounter))
            #             #Pasamos el proceso a la tabla de terminados
            #             self.insertRow(self.queue.dequeue())
            #         counter -= 1
            #         self.textBox_restantes.setText(str(counter-1))
            #     else:
            #         self.textBox_restantes.setText(str(0))
            #         break
            # self.textBox_restantes.setText(str(0))
            # self.tablaProcesos.clearContents()
        
    
    def insertBatch(self,batch:list):
        self.tablaProcesos.clearContents()
        for i in range(len(batch)):
            n = self.tablaProcesos.rowCount()
            self.tablaProcesos.insertRow(n)
            self.tablaProcesos.setItem(n,0,QTableWidgetItem(batch[i].getID()))
            self.tablaProcesos.setItem(n,1,QTableWidgetItem(str(batch[i].getTime())))
            self.tablaProcesos.setItem(n,2,QTableWidgetItem(batch[i].getFullOperation()))
    
    def insertRow(self,row:Process,batch:int):
        n = self.tablaPTerminados.rowCount()
        self.tablaPTerminados.insertRow(n)
        self.tablaPTerminados.setItem(n,0,QTableWidgetItem(str(batch)))
        self.tablaPTerminados.setItem(n,1,QTableWidgetItem(row.getID()))
        self.tablaPTerminados.setItem(n,2,QTableWidgetItem(row.getFullOperation()))
        self.tablaPTerminados.setItem(n,3,QTableWidgetItem(str(row.getResult())))