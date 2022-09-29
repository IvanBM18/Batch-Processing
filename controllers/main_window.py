#e = 101 (E/S) Ejecución pasa a bloqueados durante 7 seg, luego a listos
# W = 119 (Error)
# P = 112
# c = 99
#Cambio de Batch, forza cambio automatico de proceso en la cola
#Nuevo
# Listos: Procesos en la cola de ejecución
# Bloquados: Procesos que no se pueden ejecutar hasta que termine una operación de E/S
# Terminado: Procesos que se salieron de procesos activos

# Adaptar para que el programa siga, aunque no haya proceso en listo, pero si en E/S

#Library Imports
import keyboard
import random
from typing import Any

# QT Imports
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from PySide6.QtCore import QTimer

#UI Imports
from view.ui_mainwindow import Ui_MainWindow as MainWindow

#Class Imports
from models.queue import Queue
from models.process import Process
from models.batch import Batch
from models.uiUpdate import Updates

class MainForm(QMainWindow, MainWindow):
#Atributtes
    # Process Variables
    totalProcess : int = 0
    # Batch with all new Processes
    readyProcesses = Batch() 
    #Ready Queue
    newQueue = Queue() #Cola de Procesos Listos
    #Blocked List
    blockedList = []
    # Finished Process List
    finishedList = []

    #Variables used in Counting
    counting = False #Bandera para iniciar el proceso de ejecucion
    timer : QTimer  #Timer que se ejecuta cada segundo para actualizar el contador global
    
    #Variables to be used during process Execution
    actualProcess : Process
    timeCounter = 0 #Contador de Tiempo Global
    elapsedTime = 0 #Contador de Tiempo de Proceso
    remainingTime = 0 #Tiempo restante del proceso
    indxP = 0 #Indice del proceso en el batch en ejecución, en creación indice actual
    interruptedProcesses = False
    
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
        #Button Listeners
        self.pushButton_Agregar.clicked.connect(self.setTotalProcess)
        self.pushButton_Ejecutar.clicked.connect(self.startExecution)
        self.pushButton_Ejecutar.setEnabled(False)
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
            if(self.newQueue.getLength() != 0):
                self.newQueue = Queue()
                self.readyProcesses = Batch()
            self.totalProcess = int(validateEntry)
            self.pushButton_Ejecutar.setEnabled(True)
    
#Processing Methods
    #Counting Method
    def updateTimer(self):
        # Eliminar repeticion de set text timeCounter
        uiChangeFlag = False
        if(self.counting == True):
            # Pushing Process to Finished Queue by Error
            if(self.error == True):
                self.remainingTime = 0
            if(self.interruptedProcesses):
                self.updateUI(Updates.BLOCKED)
            # Interrupting Actual Process
            if(self.interruption): #Send process to bloqued List
                self.actualProcess.setElapsedTime(self.elapsedTime)
                # Removing and adding to Table
                self.tablaProcesos.removeRow(0)
                
                # ReEnqueueing Process
                self.readyProcesses.removeProcess()
                self.actualProcess.setBlockedTime(7)
                self.blockedList.append(self.actualProcess)
                self.insertBloquedRow(self.actualProcess)
                
                # Adding new process to ready List
                if(self.newQueue.getLength() > 0):
                    aux = self.newQueue.dequeue()
                    self.readyProcesses.addProcess(aux)
                    self.insertReadyRow(aux)
                    aux.stats.setArrivalTime(self.timeCounter)
                    
                
                # Adapting Variables to Interruption
                self.actualProcess = self.readyProcesses.getTopProcess()
                self.elapsedTime = self.actualProcess.getElapsedTime() #Tiempo transcurrido del proceso
                self.remainingTime = self.actualProcess.getTime() #Tiempo restante del proceso
                
                # Adapting UI to Interruption
                self.updateUI(Updates.NEW)
                
                # Resetting Interruption Flag
                self.interruption = False
                self.interruptedProcesses = True
                
                return
            # Fin del Procesamiento
            if ((self.newQueue.getLength() == 0) and (self.readyProcesses.getRemainingProcess() == 0) and (self.remainingTime == 0) and (len(self.blockedList) == 0)): 
                self.textBox_restantes.setText(str(0))
                self.tablaProcesos.clearContents()
                self.counting = False
                print("Procesamiento Terminado!")
                # Last process calculations
                self.actualProcess.stats.setEndTime(self.timeCounter)
                self.actualProcess.stats.setTotalTime(self.timeCounter - self.actualProcess.stats.getAnswerTime())
                self.actualProcess.stats.setWaitTime(self.actualProcess.stats.getTotalReturnTime() - self.actualProcess.stats.getServiceTime())
                if(self.error):
                    self.actualProcess.stats.setServiceTime(self.actualProcess.stats.getEndTime() - self.actualProcess.stats.getAnswerTime())
                else:
                    self.actualProcess.stats.setServiceTime(self.actualProcess.getTime())
                self.finishedList.append(self.actualProcess)
                self.updateUI(Updates.END)
                return
            # Caso 0
            if(self.readyProcesses.getRemainingProcess() == 0): 
                # Enqueueing first 3 processes
                for i in range(3):
                    aux = self.newQueue.dequeue()
                    aux.stats.setArrivalTime(self.timeCounter)
                    self.readyProcesses.addProcess(aux)
                    self.insertReadyRow(aux)
                # Time changes
                self.elapsedTime = 0
                self.actualProcess = self.readyProcesses.getTopProcess() #Proceso Actual
                self.remainingTime = self.actualProcess.getTime() #Tiempo restante del proceso
                
                self.updateUI(Updates.NEW)
                uiChangeFlag = True
                return
            #Cambio de Proceso
            if(self.remainingTime == 0): 
                
                # Insert Process to Finished Table
                self.insertFinishedRow(self.actualProcess,self.error)
                if(self.error):
                    self.error = False
                self.tablaProcesos.removeRow(0)
                
                # Enqueueing new Process
                self.readyProcesses.removeProcess()
                if(self.newQueue.getLength() != 0 and self.readyProcesses.getRemainingProcess() < 3):
                    aux = self.newQueue.dequeue()
                    self.insertReadyRow(aux)
                    aux.stats.setArrivalTime(self.timeCounter)
                    self.readyProcesses.addProcess(aux)
                
                # Process Counter Update
                self.textBox_restantes.setText(str(self.readyProcesses.getRemainingProcess()))
                
                # End of process time changes
                self.actualProcess.stats.setEndTime(self.timeCounter)
                self.actualProcess.stats.setTotalTime(self.timeCounter - self.actualProcess.stats.getAnswerTime())
                self.actualProcess.stats.setWaitTime(self.actualProcess.stats.getTotalReturnTime() - self.actualProcess.stats.getServiceTime())
                if(self.error):
                    self.actualProcess.stats.setServiceTime(self.actualProcess.stats.getEndTime() - self.actualProcess.stats.getAnswerTime())
                else:
                    self.actualProcess.stats.setServiceTime(self.actualProcess.getTime())
                
                
                if(self.readyProcesses.getRemainingProcess() != 0): #Si quedan aun procesos
                    #Obtenemos un nuevo proceso
                    self.finishedList.append(self.actualProcess)
                    self.actualProcess = self.readyProcesses.getTopProcess() 
                    
                    
                    if(self.actualProcess.getElapsedTime() != 0):
                        self.elapsedTime = self.actualProcess.getElapsedTime()
                        self.remainingTime = self.actualProcess.getTime() - self.elapsedTime
                    else:
                        self.actualProcess.stats.setAnswerTime(self.timeCounter-self.actualProcess.stats.getArrivalTime())
                        self.elapsedTime = 0 
                        self.remainingTime = self.actualProcess.getTime() #Tiempo restante del proceso
                        
                    self.updateUI(Updates.NEW)
                    return
            #Continuamos con el proceso actual
            elif(not uiChangeFlag): 
                self.timeCounter += 1
                self.elapsedTime += 1
                self.remainingTime -= 1
                self.updateUI(Updates.UPDATE)
                return
    
    #Starts Batch Processing
    def startExecution(self):
        self.tablaPTerminados.clearContents()
        if(self.totalProcess != 0):
            self.timeCounter = 0 #Contador de Tiempo Global
            self.elapsedTime = 0 #Contador de Tiempo de Proceso
            self.remainingTime = 0 #Tiempo restante del proceso
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
            newProcess = Process((random.randint(1,100)),(random.randint(1,100)),operation,(random.randint(6,16)),self.indxP)
            self.indxP +=1
        return newProcess
    
    #Generate new Process
    def generateProcess(self):
        if(self.totalProcess > 0):
            cont = 0
            newProcess : Process
            while(cont < self.totalProcess):
                newProcess = self.newProcess()
                self.newQueue.enqueue(newProcess)
                cont += 1
            self.indxP = 0
    
#Visual Methods
    def updateUI(self,upType) -> None:
        #New Process on Execution
        if(upType == Updates.NEW):
            self.textBox_tiempo_transcurrido.setText(str(self.elapsedTime))
            self.textBox_tiempo_restante.setText(str(self.remainingTime))
            self.textBox_operacion.setText(self.actualProcess.getFullOperation())
            self.textBox_Id_proceso.setText(str(self.actualProcess.getID()))
            self.textBox_restantes.setText(str(self.newQueue.getLength()))
        #Only Changes in Remaining Time/Elapsed Time
        if(upType == Updates.UPDATE):
            self.textBox_tiempo_transcurrido.setText(str(self.elapsedTime))
            self.textBox_tiempo_restante.setText(str(self.remainingTime))
        #Blocked Process
        if(upType == Updates.BLOCKED):
            cont = 0
            time : int
            for i in self.blockedList:
                if(i.getBlockedTime() != 0):
                    i.setBlockedTime(i.getBlockedTime() - 1)
                    time = i.getBlockedTime()
                    self.tablaPbloqueados.setItem(cont,1,QTableWidgetItem(str(time)))
                else:
                    self.readyProcesses.addProcess(i)
                    self.insertReadyRow(i)
                    self.tablaPbloqueados.removeRow(0)
                    self.blockedList.remove(i)
                cont += 1
        # End of Processing
        if(upType == Updates.END):
            for i in self.finishedList:
                self.insertTimeRow(i)
        self.textBox_contadorGlobal.setText(str(self.timeCounter))
        
    # Inserts row in ProcessTable
    def insertReadyRow(self,process:Process):
        n = self.tablaProcesos.rowCount()
        self.tablaProcesos.insertRow(n)
        self.tablaProcesos.setItem(n,0,QTableWidgetItem(str(process.getID())))
        self.tablaProcesos.setItem(n,1,QTableWidgetItem(str(process.getTime())))
        self.tablaProcesos.setItem(n,2,QTableWidgetItem(str(process.getElapsedTime())))
    
    #Insert row in Bloqued Table
    def insertBloquedRow(self,process:Process):
        n = self.tablaPbloqueados.rowCount()
        self.tablaPbloqueados.insertRow(n)
        self.tablaPbloqueados.setItem(n,0,QTableWidgetItem(str(process.getID())))
        self.tablaPbloqueados.setItem(n,1,QTableWidgetItem(str(process.getBlockedTime())))
    
    #Insert row in Time Table
    def insertTimeRow(self,process:Process):
        n = self.tablePTimeStats.rowCount()
        stat = process.stats
        self.tablePTimeStats.insertRow(n)
        self.tablePTimeStats.setItem(n,0,QTableWidgetItem(str(process.getID())))
        self.tablePTimeStats.setItem(n,1,QTableWidgetItem(str(stat.getArrivalTime())))
        self.tablePTimeStats.setItem(n,2,QTableWidgetItem(str(stat.getEndTime())))
        self.tablePTimeStats.setItem(n,3,QTableWidgetItem(str(stat.getTotalReturnTime())))
        self.tablePTimeStats.setItem(n,4,QTableWidgetItem(str(stat.getAnswerTime())))
        self.tablePTimeStats.setItem(n,5,QTableWidgetItem(str(stat.getWaitTime())))
        self.tablePTimeStats.setItem(n,6,QTableWidgetItem(str(stat.getServiceTime())))
    
    #Inserts a row in the finished Table
    def insertFinishedRow(self,row:Process,errorFlag:bool):
        n = self.tablaPTerminados.rowCount()
        self.tablaPTerminados.insertRow(n)
        self.tablaPTerminados.setItem(n,0,QTableWidgetItem(str(row.getID())))
        self.tablaPTerminados.setItem(n,1,QTableWidgetItem(row.getFullOperation()))
        # If process finished with an error
        if(errorFlag):
            self.tablaPTerminados.setItem(n,2,QTableWidgetItem("Error"))
        else:
            self.tablaPTerminados.setItem(n,2,QTableWidgetItem(str(row.getResult())))