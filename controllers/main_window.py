# E = 101 (E/S) Ejecución pasa a bloqueados durante 7 seg, luego a listos
# W = 119 (Error)
# P = 112 (Pausa)
# C = 99 (Continuar)
# N = 110 (Nuevo) Al presionar N se crea un nuevo proceso
# B = 98 (Tabla de PCB) Pausa y con C continuas
# Fin de Quantum Agrega a la cola de listos, no a la de nuevos
# Listos: Procesos en la cola de ejecución
# Bloquados: Procesos que no se pueden ejecutar hasta que termine una operación de E/S
# Terminado: Procesos que se salieron de procesos activos

# Tabla BCP, Mostrar casilla vacia en lugar de  -1 en los tiempos

#Library Imports
import keyboard
import random
from typing import List
from time import sleep

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
from models.uiUpdate import Updates
from models.memory import Memory

class MainForm(QMainWindow, MainWindow):
#Atributtes
    # BCP Window
    BCPWindow : BCP_table

# Process Variables
    totalProcess = 0
    # Batch with all new Processes
    readyProcesses = []
    #Ready Queue
    newQueue = Queue() #Cola de Procesos Listos
    #Blocked List
    blockedProcesses = []
    # Finished Process List
    finishedList = []
    # Updates the actual process Index
    indxP = 0
    
#Variables used in Counting
    timer : QTimer = None  #Timer que se ejecuta cada segundo para actualizar el contador global
    quantum = 0 #Quantum Measure
    quantumCounter = 0 #Quantum Counter
    timeCounter = 0 #Contador de Tiempo Global
    elapsedTime = 0 #Contador de Tiempo de Proceso transcurrido
    remainingTime = 0 #Contador Tiempo restante del proceso
    
#Variables to be used during process Execution
    actualProcess : Process
    BCPWindow  : BCP_table
    interruptedProcesses = False
    memory : Memory 
    
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
        self.setWindowTitle("Round-Robin (RR)")
        # Timer Generation
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.updateTimer)
        #Button Listeners
        self.pushButton_Agregar.clicked.connect(self.setValues)
        self.pushButton_Ejecutar.clicked.connect(self.startExecution)
        self.pushButton_Ejecutar.setEnabled(False)
        
        keyboard.on_press(self.onKeyPress)
        
        self.progressBar_43.setStyleSheet("QProgressBar::chunk{background-color: red;}")
        self.progressBar_42.setStyleSheet("QProgressBar::chunk{background-color: red;}")
        self.progressBar_41.setStyleSheet("QProgressBar::chunk{background-color : red;}")
        self.progressBar_40.setStyleSheet("QProgressBar::chunk{background-color: red;}")
        self.progressBar_40.setValue(100)
    
#Setters
    def setValues(self):
        self.setTotalProcess()
        self.setQuantum()

    def setTotalProcess(self):
        validateEntry = self.textBox_NumProcess.text()
        if (not str(validateEntry).isdigit() or validateEntry == "" or int(validateEntry) <= 0):
            print("[ERROR] introduce un numero")
            msgBox = QMessageBox()
            msgBox.setText("Introduce un numero válido")
            msgBox.setWindowTitle("ERROR en Numero de Procesos")
            msgBox.exec_()
            self.textBox_NumProcess.setText("")
        else:
            if(self.newQueue.getLength() != 0):
                self.newQueue = Queue()
                self.readyProcesses = []
            self.totalProcess = int(validateEntry)
    
    def setQuantum(self):
        validateEntry = self.textBox_Quantum.text()
        if (not str(validateEntry).isdigit() or validateEntry == "" or int(validateEntry) <= 0):
            print("[ERROR] introduce un numero")
            msgBox = QMessageBox()
            msgBox.setText("Introduce un numero válido")
            msgBox.setWindowTitle("ERROR en Quantum")
            msgBox.exec_()
            self.textBox_Quantum.setText("")
        else:
            self.quantum = int(validateEntry)
            self.pushButton_Ejecutar.setEnabled(True)
#Getters
    # Returns all process wherever they are
    def getAllProcesses(self) -> List[Process]:
        aux =[]
        result = []
        aux += self.newQueue.getList()
        aux += self.blockedProcesses
        aux += self.readyProcesses
        aux += self.finishedList
        aux.sort(key=lambda x: x.processID)
        for i in aux:
            result.append(self.updateTStats(i))
        return result
    
    # Returns a color in hexadecimal
    def getRandomRGBColor(self) -> str:
        randomColor = "#".join([str(hex(random.randint(0, 255)))[2:] for _ in range(3)])
        return randomColor
    
#Processing Methods
    # Updates the timer and the UI
    def updateTimer(self):
        # Eliminar repeticion de set text timeCounter
        
        # Pausado por tabla de PCB
        if(self.bcp):
            self.timer.stop()
            self.BCPWindow = BCP_table(self.getAllProcesses())
            self.BCPWindow.startTable()
            
            self.BCPWindow.show()
            # Ciclo para mantener la ventana de BCP abierta
            while self.pause:
                QCoreApplication.processEvents()
            self.BCPWindow.hide()
            
            self.bcp = False
            self.pause = False
            self.timer.start(1000)
        
        if(not self.pause):
            # Pushing Process to Finished Queue by Error
            if(self.error):
                self.remainingTime = 0
            
            # If there is a process bloqued
            if(self.interruptedProcesses):
                self.updateUI(Updates.BLOCKED)
            
            # Interrupting Actual Process
            if(self.interruption):
                if(self.actualProcess):
                    self.onInterruption()
                QCoreApplication.processEvents()
            
            # End of Processing
            if(self.noProcessesLeft()): 
                self.actualProcess.stats.setEndTime(self.timeCounter)
                self.actualProcess = self.updateTStats(self.actualProcess)
                if(self.error):
                    self.actualProcess.stats.setServiceTime(self.actualProcess.stats.getEndTime() - self.actualProcess.stats.getAnswerTime())
                else:
                    self.actualProcess.stats.setServiceTime(self.actualProcess.getTime())
                self.finishedList.append(self.actualProcess)
                
                #Updating UI
                self.updateUI(Updates.END)
                print("Procesamiento Terminado!")
                self.timer.stop()
                return
            
            # Proccess Change
            if(self.isChangeNeeded()):
                # Removing Process from Ready Queue
                self.tablaProcesos.removeRow(0) 
                self.readyProcesses.pop(0) 
                
                # Change due to Quantum
                if(not self.quantumCounter and self.remainingTime ):
                    self.onQuantumEnd()
                    QCoreApplication.processEvents()
                # Change due time end
                else:
                    # End of process time stats
                    self.actualProcess.remainingTime = 0
                    self.actualProcess.stats.setEndTime(self.timeCounter)
                    self.actualProcess = self.updateTStats(self.actualProcess)
                    if(self.error):
                        self.actualProcess.stats.setServiceTime(self.actualProcess.stats.getEndTime() - self.actualProcess.stats.getAnswerTime())
                        self.actualProcess.error = True
                        self.error = False
                    else:
                        self.actualProcess.stats.setServiceTime(self.elapsedTime)
                    
                    # Insert Process to Finished Table
                    self.insertFinishedRow(self.actualProcess,self.error)
                    self.finishedList.append(self.actualProcess)
                    
                # Enqueueing new Process to ready List
                if(self.newQueue.getLength() and len(self.readyProcesses) < 3):
                    aux = self.newQueue.dequeue()
                    aux.stats.setArrivalTime(self.timeCounter)
                    self.readyProcesses.append(aux)
                    self.insertReadyRow(aux)
                    
                # Setting a new actual Process
                if(self.readyProcesses): 
                    #Gain a new process
                    self.actualProcess : Process = self.readyProcesses[0] 
                    self.elapsedTime = self.actualProcess.getElapsedTime()
                    
                    # Calculating new remaining time
                    if(self.elapsedTime):
                        self.remainingTime = self.actualProcess.getTime() - self.elapsedTime
                    # Completely new Process
                    else:
                        #Tiempo restante del proceso
                        self.actualProcess.stats.setAnswerTime(self.timeCounter-self.actualProcess.stats.getArrivalTime())
                        self.remainingTime = self.actualProcess.getTime() 
                        
                    self.updateUI(Updates.NEW)
                return
            #Normal Execution
            else: 
                self.timeCounter += 1
                self.elapsedTime += 1
                self.remainingTime -= 1
                self.quantumCounter -= 1
                self.updateUI(Updates.TIMER)
    
    # Execute Lot Processing
    def execute(self):
        
        while(not self.noProcessesLeft()):
            if(self.pause):
                continue
            # Ending Process due to error
            if(self.error): 
                self.remainingTime = 0
                
            # If there is a process bloqued
            if(self.interruptedProcesses):
                self.updateUI(Updates.BLOCKED)
            
            # Interrupting Actual Process
            if(self.interruption):
                if(self.actualProcess):
                    self.onInterruption()
                    QCoreApplication.processEvents()
            
            # Process Change
            if(self.isChangeNeeded()):
                # Removing Process from Ready Queue
                self.tablaProcesos.removeRow(0) 
                self.readyProcesses.pop(0) 
                
                # Change due to Quantum
                if(not self.quantumCounter and self.remainingTime):
                    self.onQuantumEnd()
                    QCoreApplication.processEvents()
                # Change due proceess end
                else:
                    self.onProcessEnd()
                    
                # Enqueueing new Process to ready List
                if(self.newQueue.getLength() and len(self.readyProcesses) < 3):
                    # If Theres Memory Space Available
                    auxMemory = self.memory.reserveMemory(self.newQueue.getFront().getSize())
                    if(auxMemory != None):
                        aux : Process = self.newQueue.dequeue()
                        aux.setPageList(auxMemory)
                        aux.stats.setArrivalTime(self.timeCounter)
                        self.readyProcesses.append(aux)
                        self.insertReadyRow(aux)
                    
                # Geting a new actual Process
                if(self.readyProcesses):
                    self.onNewProcess()
                    
                QCoreApplication.processEvents()
                    
            self.timeCounter += 1
            self.elapsedTime += 1
            self.remainingTime -= 1
            self.quantumCounter -= 1
            self.updateUI(Updates.TIMER)
            QCoreApplication.processEvents()
            sleep(1)
        
        if(self.noProcessesLeft()):
            self.endExecution()
    
    #Starts Task Processing
    def startExecution(self) -> None:
        self.tablaPTerminados.clearContents()
        self.tablaPbloqueados.clearContents()
        self.tablaProcesos.clearContents()
        
        if(self.totalProcess != 0):
            self.memory = Memory()
            self.timeCounter = 0 #Contador de Tiempo Global
            self.elapsedTime = 0 #Contador de Tiempo de Proceso
            self.remainingTime = 0 #Tiempo restante del proceso
            self.generateProcesses()
            self.pause = False
            for _ in range(3):
                if(self.newQueue.getLength() > 0):
                    aux : Process = self.newQueue.dequeue()
                    aux.stats.setArrivalTime(self.timeCounter)
                    aux.setPageList(self.reserveSpace(aux.getSize()))
                    self.readyProcesses.append(aux)
                    self.insertReadyRow(aux)
                    
            # Time changes
            self.elapsedTime = 0
            self.actualProcess : Process = self.readyProcesses[0] #Proceso Actual
            self.remainingTime = self.actualProcess.getTime() #Tiempo restante del proceso
            self.actualProcess.stats.setAnswerTime(self.timeCounter)
            self.quantumCounter = self.quantum
            
            self.textBox_quantumGlobal.setText(str(self.quantum))
            self.updateUI(Updates.NEW)
            QCoreApplication.processEvents()
            self.execute()
    
    # End of Processing
    def endExecution(self):
        # Last process calculations
        self.actualProcess.stats.setEndTime(self.timeCounter)
        self.actualProcess = self.updateTStats(self.actualProcess)
        if(self.error):
            self.actualProcess.stats.setServiceTime(self.actualProcess.stats.getEndTime() - self.actualProcess.stats.getAnswerTime())
        else:
            self.actualProcess.stats.setServiceTime(self.actualProcess.getTime())
        self.finishedList.append(self.actualProcess)
        
        #Updating UI
        self.updateUI(Updates.END)
    
        print("Procesamiento Terminado!")
    
    # Applies on keyboard press
    def onKeyPress(self,event):
        try:
            option = str(event.name).lower()
            # print(f'Key {event.name} pressed')
            # Pause
            if(option == 'p'): 
                self.pause = True
            # Continue
            elif(option == 'c'):
                if(self.pause):
                    self.pause = False
                    self.bcp = False
                else:
                    self.pause = False
                    self.bcp = False
                
            # Interrupt
            elif(option == 'e'):
                print("Interrupcion")
                self.interruption = True
            # Error
            elif(option == 'w'):
                print("Error")
                self.error = True
            # New Process
            elif(option == 'n'):
                # Generating and Enqueueing new process
                aux = self.newProcess(self.indxP)
                self.indxP += 1
                aux.stats.setArrivalTime(self.timeCounter)
                if(len(self.readyProcesses) < 3):
                    self.readyProcesses.append(aux)
                    self.insertReadyRow(aux)
                else:
                    self.newQueue.enqueue(aux)
                self.textBox_restantes.setText(str(self.newQueue.getLength()))
            # BCP Table
            elif(option == 'b'):
                self.bcp = True
                self.pause = True

                self.BCPWindow = BCP_table(self.getAllProcesses())
                self.BCPWindow.startTable()
                
                self.BCPWindow.show()
                # Ciclo para mantener la ventana de BCP abierta
                while self.pause:
                    QCoreApplication.processEvents()
                self.BCPWindow.hide()
        except:
            pass
    
    # Processes left comprobation
    def noProcessesLeft(self):
        if(self.newQueue.getLength()):
            return False
        if(len(self.readyProcesses)):
            return False
        if(len(self.blockedProcesses)):
            return False
        if(self.remainingTime):
            return False
        return True

    # Asks if process Ends
    def isChangeNeeded(self) -> bool:
        if(not self.quantumCounter):
            return True
        if(not self.remainingTime):
            return True
        if(not self.actualProcess):
            return True
        
        return False

#Process Creation/Maniuplation
    #Generate new Process
    def newProcess(self,indexP : int) -> Process:
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
            newProcess = Process((random.randint(1,100)),(random.randint(1,100)),operation,(random.randint(6,16)),indexP,(random.randint(6,28)))
        return newProcess
    
    #Generate new Process
    def generateProcesses(self) -> None:
        if(self.totalProcess > 0):
            cont = 0
            newProcess : Process
            while(cont < self.totalProcess):
                newProcess = self.newProcess(cont)
                self.newQueue.enqueue(newProcess)
                cont += 1
            self.indxP = cont
    
    # Update Time Stats
    def updateTStats(self,p : Process) -> Process:
        # Si ya termino su ejecución
        if(p.getTime() == 0):
            p.stats.setReturnTime(p.stats.getEndTime() - p.stats.getArrivalTime())
        # Si aun no termina su ejecución, pero ya entro a la cola de listos
        if(p.stats.getArrivalTime() != -1):
            p.stats.setWaitTime(self.timeCounter - p.stats.getArrivalTime() - p.stats.getServiceTime())
        # Si es el que se esta ejecutando actualmente
        if(self.actualProcess.getID() == p.getID()):
            p.stats.setServiceTime(self.elapsedTime)
        return p
    
    # Handles the process change
    def onNewProcess(self) -> None:
        #Gain a new process
        self.actualProcess : Process = self.readyProcesses[0] 
        self.elapsedTime = self.actualProcess.getElapsedTime()
        
        # Calculating new remaining time
        if(self.elapsedTime):
            self.remainingTime = self.actualProcess.getTime() - self.elapsedTime
        # New Process
        else:
            #Tiempo restante del proceso
            self.actualProcess.stats.setAnswerTime(self.timeCounter-self.actualProcess.stats.getArrivalTime())
            self.remainingTime = self.actualProcess.getTime() 
            
        self.updateUI(Updates.NEW)
    
    # Handles Process Interruption
    def onInterruption(self) -> None:
        #Send process to bloqued List
        self.actualProcess.setElapsedTime(self.elapsedTime)
        self.actualProcess = self.updateTStats(self.actualProcess)
        # Removing and adding to Table
        self.tablaProcesos.removeRow(0)
        self.readyProcesses.pop(0)
        
        # ReEnqueueing Process
        self.actualProcess.setBlockedTime(7)
        self.blockedProcesses.append(self.actualProcess)
        self.insertBloquedRow(self.actualProcess)
        
        # Adding new process to ready List
        if(self.newQueue.getLength() and len(self.readyProcesses) < 3):
            aux : Process = self.newQueue.dequeue()
            self.readyProcesses.append(aux)
            self.insertReadyRow(aux)
            aux.stats.setArrivalTime(self.timeCounter)
        
        if(len(self.readyProcesses)):
            # Adapting Variables to Interruption
            self.actualProcess = self.readyProcesses[0]
            self.elapsedTime = self.actualProcess.getElapsedTime() #Tiempo transcurrido del proceso
            self.remainingTime = self.actualProcess.getTime() #Tiempo restante del proceso
        # If there are no more processes in the new Queue
        else:
            self.actualProcess = None
            self.remainingTime = 7
            self.elapsedTime = 0
        
        # Adapting UI to Interruption
        self.updateUI(Updates.NEW)
        
        # Resetting Interruption Flag
        self.interruption = False
        self.interruptedProcesses = True
    
    # Handles Quantum Expiration
    def onQuantumEnd(self) -> None:
        #Send process to ready List
        self.actualProcess.setElapsedTime(self.elapsedTime)
        self.actualProcess = self.updateTStats(self.actualProcess)
        # Removing and adding to Table
        self.insertReadyRow(self.actualProcess)
        self.readyProcesses.append(self.actualProcess)
        self.quantumCounter = self.quantum        
    
    # Handles Process End
    def onProcessEnd(self) -> None:
        self.actualProcess.remainingTime = 0
        self.actualProcess.stats.setEndTime(self.timeCounter)
        self.actualProcess = self.updateTStats(self.actualProcess)
        if(self.error):
            self.actualProcess.stats.setServiceTime(self.actualProcess.stats.getEndTime() - self.actualProcess.stats.getAnswerTime())
            self.actualProcess.error = True
            self.error = False
        else:
            self.actualProcess.stats.setServiceTime(self.elapsedTime)
        
        # Insert Process to Finished Table
        self.insertFinishedRow(self.actualProcess,self.error)
        self.finishedList.append(self.actualProcess)
        
        # Free Memory
        self.freeSpace(self.actualProcess.pageList)
    
#Memory Management
    # Reserves Memory for a new Process
    def reserveSpace(self,size) -> None:
        color = self.getRandomRGBColor()
        pages = self.memory.reserveMemory(size)
        for i in pages:
            self.changeTablePage(i,color)
        return pages
    
    # Frees Memory for a Process
    def freeSpace(self,pages) -> None:
        for i in pages:
            self.changeTablePage(i,"green")
        self.memory.freeMemory(pages)
    
#Visual Methods
    def updateUI(self,upType) -> None:
        #New Process on Execution
        if(upType == Updates.NEW):
            self.textBox_tiempo_transcurrido.setText(str(self.elapsedTime))
            self.textBox_tiempo_restante.setText(str(self.remainingTime))
            self.textBox_operacion.setText(self.actualProcess.getFullOperation())
            self.textBox_Id_proceso.setText(str(self.actualProcess.getID()))
            self.textBox_restantes.setText(str(self.newQueue.getLength()))
            self.quantumCounter = self.quantum
            self.textBox_quantumGlobal.setText(str(self.quantumCounter))
            # Next Process to enter Ready Queue
            if(self.newQueue.getLength()):
                self.textBox_proximo_id.setText(str(self.newQueue.getFront().getID()))
                self.textBox_proximo_size.setText(str(self.newQueue.getFront().getSize()))
        #Only Changes in Remaining Time/Elapsed Time
        if(upType == Updates.TIMER):
            self.textBox_tiempo_transcurrido.setText(str(self.elapsedTime))
            self.textBox_tiempo_restante.setText(str(self.remainingTime))
            self.textBox_quantumGlobal.setText(str(self.quantumCounter))
        #Blocked Process
        if(upType == Updates.BLOCKED):
            cont = 0
            time : int
            for i in self.blockedProcesses:
                if(i.getBlockedTime()):
                    i.setBlockedTime(i.getBlockedTime() - 1)
                    time = i.getBlockedTime()
                    self.tablaPbloqueados.setItem(cont,1,QTableWidgetItem(str(time)))
                else:
                    self.readyProcesses.append(i)
                    self.insertReadyRow(i)
                    self.tablaPbloqueados.removeRow(0)
                    self.blockedProcesses.pop(0)
                cont += 1
        # End of Processing
        if(upType == Updates.END):
            self.textBox_restantes.setText(str(0))
            self.textBox_quantumGlobal.setText(str(0))
            self.tablaProcesos.clearContents()
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
    
    # Updates the table of pages
    def changeTablePage(self,indx: int, color : str):
        if(indx == 0):
            self.progressBar.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 1):
            self.progressBar_1.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 2):
            self.progressBar_2.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 3):
            self.progressBar_3.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 4):
            self.progressBar_4.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 5):
            self.progressBar_5.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 6):
            self.progressBar_6.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 7):
            self.progressBar_7.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 8):
            self.progressBar_8.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 9):
            self.progressBar_9.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")  
        elif(indx == 10):
            self.progressBar_10.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 11):
            self.progressBar_11.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 12):
            self.progressBar_12.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 13):
            self.progressBar_13.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 14):
            self.progressBar_14.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 15):
            self.progressBar_15.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 16):
            self.progressBar_16.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 17):
            self.progressBar_17.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 18):
            self.progressBar_18.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 19):
            self.progressBar_19.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 20):
            self.progressBar_20.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 21):
            self.progressBar_21.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 22):
            self.progressBar_22.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 23):
            self.progressBar_23.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 24):
            self.progressBar_24.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 25):
            self.progressBar_25.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 26):
            self.progressBar_26.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 27):
            self.progressBar_27.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 28):
            self.progressBar_28.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 29):
            self.progressBar_29.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 30):
            self.progressBar_30.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 31):
            self.progressBar_31.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 32):
            self.progressBar_32.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 33):
            self.progressBar_33.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 34):
            self.progressBar_34.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 35):
            self.progressBar_35.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 36):
            self.progressBar_36.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 37):
            self.progressBar_37.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 38):
            self.progressBar_38.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        elif(indx == 39):
            self.progressBar_39.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
        else:
            return