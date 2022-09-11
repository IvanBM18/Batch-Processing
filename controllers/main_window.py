#e = 101
# W = 119
# P = 112
# c = 99
#Cambio de Batch, forza cambio automatico de proceso en la cola
from http.client import GONE
import keyboard
import random
from typing import Any
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from PySide6.QtCore import QTimer

from view.ui_mainwindow import Ui_MainWindow as MainWindow
from models.queue import Queue
from models.process import Process
from models.batch import Batch


class MainForm(QMainWindow, MainWindow):
    
#Atributtes
    # Process Atributes
    totalProcess : int = 0
    queue = Queue() #Cola de Lotes
    batch = Batch() #Batch Actual

    #Variables used in Counting
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
    
    #Flags for keyboard Press
    pause = False
    error = False
    interruption = False
    
    #Constructor
    def __init__(self):
        super().__init__()
        #Generating Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTimer)
        self.timer.start(1000)
        #Init UI
        self.setupUi(self)
        #Initial configurations
        self.pushButton_Agregar.clicked.connect(self.setTotalProcess)
        self.pushButton_ejecturar.clicked.connect(self.processBatches)
        self.pushButton_ejecturar.setEnabled(False)
        #Keboard Listener
        keyboard.on_press(self.onKeyPress)
        
    
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
    #Counting Method
    def updateTimer(self):
        uiChangeFlag = False
        # Eliminar repeticion de set text timeCounter
        if(self.counting == True):
            # Pushing Process to Finished Queue by Error
            if(self.error == True):
                self.remainingTime = 0
            # Interrupting Actual Process
            if(self.interruption):
                self.actualProcess.setElapsedTime(self.elapsedTime)
                # Removing and adding to Table
                self.tablaProcesos.removeRow(0)
                self.insertProcessingRow(self.actualProcess)
                
                # ReEnqueueing Process
                self.batch.removeProcess()
                self.batch.addProcess(self.actualProcess)
                
                # Adapting Variables to Interruption
                self.actualProcess = self.batch.getTopProcess()
                self.elapsedTime = 0 #Tiempo transcurrido del proceso
                self.remainingTime = self.actualProcess.getTime() #Tiempo restante del proceso
                
                # Adapting UI to Interruption
                self.textBox_tiempo_transcurrido.setText(str(self.elapsedTime))
                self.textBox_tiempo_restante.setText(str(self.remainingTime))
                self.textBox_operacion.setText(self.actualProcess.getFullOperation())
                self.textBox_Id_proceso.setText(str(self.actualProcess.getID()))
                
                self.interruption = False
                return
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
                uiChangeFlag = True
            if(self.batch.getRemainingProcess() == 0): #Batch Change
                self.tablaProcesos.clearContents()
                if(self.queue.getLength() != 0): #Si quedan aun batches
                    self.batch = self.queue.dequeue()       
                    self.insertBatch(self.batch.getProcessList())
                self.counter -=1
                self.textBox_restantes.setText(str(self.counter))
                self.batchCounter += 1 
                # Cambio de Proceso
                self.actualProcess = self.batch.getTopProcess()
                self.remainingTime = self.actualProcess.getTime()
                self.elapsedTime = 0
                self.textBox_operacion.setText(self.actualProcess.getFullOperation())
                self.textBox_Id_proceso.setText(str(self.actualProcess.getID()))
            #Cambio de Proceso
            if(self.remainingTime == 0): 
                self.insertFinishedRow(self.actualProcess,self.error)
                if(self.error == True):
                    self.error = False
                self.tablaProcesos.removeRow(0)
                self.batch.removeProcess()
                self.remainingTime = 0
                if(self.batch.getRemainingProcess() != 0): #Si quedan aun procesos
                    self.elapsedTime = 0 #Tiempo transcurrido del proceso
                    self.actualProcess = self.batch.getTopProcess() #Obtenemos un nuevo proceso
                    if(self.actualProcess.getElapsedTime() != 0):
                        self.remainingTime = self.actualProcess.getTime() - self.actualProcess.getElapsedTime()
                        self.elapsedTime = self.actualProcess.getElapsedTime()
                    else:
                        self.remainingTime = self.actualProcess.getTime() #Tiempo restante del proceso
                    self.textBox_tiempo_transcurrido.setText(str(self.elapsedTime))
                    self.textBox_tiempo_restante.setText(str(self.remainingTime))
                    self.textBox_operacion.setText(self.actualProcess.getFullOperation())
                    self.textBox_Id_proceso.setText(str(self.actualProcess.getID()))
            elif(not uiChangeFlag): #Continuamos con el proceso
                self.timeCounter += 1
                self.elapsedTime += 1
                self.remainingTime -= 1
                self.textBox_tiempo_transcurrido.setText(str(self.elapsedTime))
                self.textBox_tiempo_restante.setText(str(self.remainingTime))
                self.textBox_contadorGlobal.setText(str(self.timeCounter))
    
    #Starts Batch Processing
    def processBatches(self):
        self.tablaPTerminados.clearContents()
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

    # Applies on keyboard press
    def onKeyPress(self,event):
        try:
            option = str(event.name).lower()
            # Pause
            if(option == 'p'): 
                self.pause = True
                self.counting = False
            # Continue
            elif(option == 'c'):
                self.pause = False
                self.counting = True
            # Interrupt
            elif(option == 'e'):
                print('e')
                self.interruption = True
            # Error
            elif(option == 'w'):
                print('w')
                self.error = True
        except:
            pass

#Process Creation
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
            newProcess = Process((random.randint(1,100)),(random.randint(1,100)),operation,(random.randint(3,5)),self.indxP)
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
    #Inserts Batches in Processing Table
    def insertBatch(self,batch:list):
        self.tablaProcesos.clearContents()
        aux : Process
        for i in range(len(batch)):
            aux = batch[i]
            self.insertProcessingRow(aux)
    
    # Inserts row in ProcessTable
    def insertProcessingRow(self,process:Process):
        n = self.tablaProcesos.rowCount()
        self.tablaProcesos.insertRow(n)
        self.tablaProcesos.setItem(n,0,QTableWidgetItem(str(process.getID())))
        self.tablaProcesos.setItem(n,1,QTableWidgetItem(str(process.getTime())))
        self.tablaProcesos.setItem(n,2,QTableWidgetItem(str(process.getElapsedTime())))
    
    #Inserts a row in the finished Table
    def insertFinishedRow(self,row:Process,errorFlag:bool):
        n = self.tablaPTerminados.rowCount()
        self.tablaPTerminados.insertRow(n)
        self.tablaPTerminados.setItem(n,0,QTableWidgetItem(str(self.batchCounter)))
        self.tablaPTerminados.setItem(n,1,QTableWidgetItem(str(row.getID())))
        self.tablaPTerminados.setItem(n,2,QTableWidgetItem(row.getFullOperation()))
        # If process finished with an error
        if(errorFlag):
            self.tablaPTerminados.setItem(n,3,QTableWidgetItem("Error"))
        else:
            self.tablaPTerminados.setItem(n,3,QTableWidgetItem(str(row.getResult())))