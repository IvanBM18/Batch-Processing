# E = 101 (E/S) Ejecución pasa a bloqueados durante 7 seg, luego a listos
# W = 119 (Error)
# P = 112 (Pausa)
# C = 99 (Continuar)
# N = 110 (Nuevo) Al presionar N se crea un nuevo proceso
# B = 98 (Tabla de PCB) Pausa y con C continuas
#Cambio de Batch, forza cambio automatico de proceso en la cola
# Listos: Procesos en la cola de ejecución
# Bloquados: Procesos que no se pueden ejecutar hasta que termine una operación de E/S
# Terminado: Procesos que se salieron de procesos activos

# Por Hacer:
# Adaptar para que el programa siga, aunque no haya proceso en listo, pero si en E/S
# Mejorar calculo de las estadisticas
# Abrir Nueva Tabla de PCB

#Library Imports
import keyboard
import random
from typing import Any

# QT Imports
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from PySide6.QtCore import QTimer, QCoreApplication

#UI Imports
from view.ui_mainwindow import Ui_MainWindow as MainWindow
from controllers.table_bcp import BCP_table

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
    timer : QTimer = None  #Timer que se ejecuta cada segundo para actualizar el contador global
    BCPWindow  : BCP_table
    
    #Variables to be used during process Execution
    actualProcess : Process
    timeCounter = 0 #Contador de Tiempo Global
    elapsedTime = 0 #Contador de Tiempo de Proceso transcurrido
    remainingTime = 0 #Contador Tiempo restante del proceso
    indxP = 0 #Indice del proceso en el batch en ejecución, en creación indice actual
    interruptedProcesses = False
    
    #Flags for keyboard Press
    pause = True
    error = False
    interruption = False
    bcp = False
    
    #Constructor
    def __init__(self):
        #Init UI
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("FCFS")
        self.BCPWindow = BCP_table()
        #Generating Timer
        # Timer Generation
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTimer)
        self.timer.start(1000)
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
    # Updates the timer and the UI
    def updateTimer(self):
        # Eliminar repeticion de set text timeCounter
        uiChangeFlag = False
        if(self.bcp):
            print("BCP")
            self.BCPWindow.show()
            while self.pause:
                QCoreApplication.processEvents()
            self.BCPWindow.hide()
            self.bcp = False
            self.pause = False
                
        if(not self.pause):
            # Pushing Process to Finished Queue by Error
            if(self.error):
                self.remainingTime = 0
            # If there is a process bloqued
            if(self.interruptedProcesses):
                self.updateUI(Updates.BLOCKED)
            # Interrupting Actual Process
            if(self.interruption):
                #Send process to bloqued List
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
            # End of Process
            if ((self.newQueue.getLength() == 0) and (self.readyProcesses.getRemainingProcess() == 0) and (self.remainingTime == 0) and (len(self.blockedList) == 0)): 
                
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
                self.textBox_restantes.setText(str(0))
                self.tablaProcesos.clearContents()
                self.counting = False
                print("Procesamiento Terminado!")
                self.timer.stop()
                return
            # Case 0
            if(self.readyProcesses.getRemainingProcess() == 0): 
                # Enqueueing first 3 processes
                for i in range(3):
                    if(self.newQueue.getLength() > 0):
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
                
                # End of process time stats
                self.actualProcess.stats.setEndTime(self.timeCounter)
                self.actualProcess.stats.setTotalTime(self.timeCounter - self.actualProcess.stats.getAnswerTime())
                self.actualProcess.stats.setWaitTime(self.actualProcess.stats.getEndTime() - self.actualProcess.stats.getArrivalTime())
                if(self.error):
                    self.actualProcess.stats.setServiceTime(self.actualProcess.stats.getEndTime() - self.actualProcess.stats.getAnswerTime())
                else:
                    self.actualProcess.stats.setServiceTime(self.actualProcess.getTime())
                
                # Try get new process
                if(self.readyProcesses.getRemainingProcess() != 0): 
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
            #Normal Execution
            elif(not uiChangeFlag): 
                self.timeCounter += 1
                self.elapsedTime += 1
                self.remainingTime -= 1
                self.updateUI(Updates.UPDATE)
    
    #Starts Task Processing
    def startExecution(self):
        self.tablaPTerminados.clearContents()
        self.tablaPbloqueados.clearContents()
        self.tablePTimeStats.clearContents()
        self.tablaProcesos.clearContents()
        if(self.totalProcess != 0):
            self.timeCounter = 0 #Contador de Tiempo Global
            self.elapsedTime = 0 #Contador de Tiempo de Proceso
            self.remainingTime = 0 #Tiempo restante del proceso
            self.generateProcesses()
            self.pause = False
            

    # Applies on keyboard press
    def onKeyPress(self,event):
        try:
            option = str(event.name).lower()
            # Pause
            if(option == 'p'): 
                self.pause = True
            # Continue
            elif(option == 'c'):
                self.pause = False
                self.bcp = False
            # Interrupt
            elif(option == 'e'):
                print('e')
                self.interruption = True
            # Error
            elif(option == 'w'):
                print('w')
                self.error = True
            # New Process
            elif(option == 'n'):
                print('n')
            # BCP Table
            elif(option == 'b'):
                self.bcp = True
                self.pause = True
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
    def generateProcesses(self) -> None:
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