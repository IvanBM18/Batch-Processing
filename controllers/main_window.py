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


# Mandar macros a archivo y extraerlos de ahi
# Colocar ID en los macros

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
from models.suspendedManager import SuspendManager

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
    # Suspended Process List
    suspendedList : SuspendManager
    # Updates the actual process Index
    indxP = 0
    
#Variables used in Counting
    quantum = 0 #Quantum Measure
    quantumCounter = 0 #Quantum Counter
    timeCounter = 0 #Contador de Tiempo Global
    elapsedTime = 0 #Contador de Tiempo de Proceso transcurrido
    remainingTime = 0 #Contador Tiempo restante del proceso
    
#Variables to be used during process Execution
    actualProcess : Process
    suspendedProcess : Process
    BCPWindow  : BCP_table
    interruptedProcesses = False
    memory : Memory 
    
#Flags for keyboard Press
    pause = True
    error = False
    interruption = False
    bcp = False
    execution = False
    
    
    #Constructor
    def __init__(self):
        #Init UI
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Programa 8 - Procesos suspendidos")
        # Timer Generation
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.updateTimer)
        #Button Listeners
        self.pushButton_Agregar.clicked.connect(self.setValues)
        self.pushButton_Ejecutar.clicked.connect(self.startExecution)
        keyboard.on_press(self.onKeyPress)
        self.pushButton_Ejecutar.setEnabled(False)
        self.suspendedList = SuspendManager()
        
        
        for i in range(40):
            self.changeTablePage(i,"lightgreen",5)
        self.progressBar_30.setStyleSheet("QProgressBar::chunk {background-color: lightgreen;}")
        self.progressBar_43.setStyleSheet("QProgressBar::chunk{background-color: red;}")
        self.progressBar_42.setStyleSheet("QProgressBar::chunk{background-color: red;}")
        self.progressBar_41.setStyleSheet("QProgressBar::chunk{background-color : red;}")
        self.progressBar_40.setStyleSheet("QProgressBar::chunk{background-color: red;}")
    
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
        randomColor = "#" + ''.join([str(hex(random.randint(0, 255)))[2:].rjust(2,'0') for _ in range(3)])
        return randomColor
    
#Processing Methods
    # Execute Lot Processing
    def execute(self):
        
        while(not self.noProcessesLeft()):
            if(self.pause):
                continue
            
            if(self.bcp):
                self.BCPWindow = BCP_table(self.getAllProcesses())
                self.BCPWindow.startTable()
                self.BCPWindow.show()
                while(self.bcp):
                    QCoreApplication.processEvents()
                    continue
                self.BCPWindow.hide()
                self.bcp = False
            
            # Ending Process due to error
            if(self.error): 
                self.remainingTime = 0
                
            # If there is a process blocked
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
                if(len(self.readyProcesses)):
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
                    auxMemory = self.reserveSpace(self.newQueue.getFront().getSize())
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
            self.execution = True
            self.execute()
    
    # End of Processing
    def endExecution(self):
        self.execution = False
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
        
        # Displaying Results
        self.BCPWindow = BCP_table(self.getAllProcesses())
        self.BCPWindow.startTable()
        self.BCPWindow.show()
        self.bcp = True
        while(self.bcp):
            QCoreApplication.processEvents()
        self.BCPWindow.hide()
        
        print("Procesamiento Terminado!")
    
    # Applies on keyboard press
    def onKeyPress(self,event):
        try:
            if(not self.execution):
                return
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
            # Pausa para tabla de paginas
            elif(option == 't'):
                self.pause = True
            # Suspender Proceso
            elif(option == 's'):
                self.onProcessSuspend()
            # Regresar Proceso
            elif(option == 'r'):
                self.getFromSuspended()
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
        if(self.remainingTime > 0):
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
            # If Theres Memory Space Available
            auxMemory = self.reserveSpace(self.newQueue.getFront().getSize())
            if(auxMemory != None):
                aux : Process = self.newQueue.dequeue()
                aux.setPageList(auxMemory)
                aux.stats.setArrivalTime(self.timeCounter)
                self.readyProcesses.append(aux)
                self.insertReadyRow(aux)
        
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
    
    # Only for blocked processes
    def onProcessSuspend(self) -> None:
        # If there are no blocked processes Ignore
        if(not self.blockedProcesses):
            return
        
        # Removing and adding to Table
        auxProcess : Process  = self.blockedProcesses.pop(0)
        self.tablaPbloqueados.removeRow(0)
        
        # Adding to suspended List
        self.suspendedList.addProcess(auxProcess)
        self.suspendedProcess = self.suspendedList.getProcessOnTop()
        
        # Freing Memory
        self.memory.freeMemory(auxProcess.pageList)
        
        self.updateUI(Updates.SUSPEND)
        self.updateUI(Updates.BLOCKED)
        return
    
    # Tries to retrieve a suspended process
    def getFromSuspended(self) -> None:
        if(self.suspendedProcess):
            auxMemory = self.reserveSpace(self.suspendedProcess.getSize())
            if(auxMemory == None):
                return
            # Adding to ready List
            aux = self.suspendedList.retrieveProcess()
            aux.setPageList(auxMemory)
            self.readyProcesses.append(aux)
            self.insertReadyRow(aux)
            
            # Getting new process from List
            self.suspendedProcess = self.suspendedList.getProcessOnTop()
            
            self.updateUI(Updates.SUSPEND)
            self.updateUI(Updates.BLOCKED)
    
#Memory Management
    # Reserves Memory for a new Process
    def reserveSpace(self,size) -> None:
        color = self.getRandomRGBColor()
        pages = self.memory.reserveMemory(size)
        if(pages):
            for i in pages:
                self.changeTablePage(i,color,5)
            self.changeTablePage(pages[-1],color,5 if size%5 == 0 else size%5)
            QCoreApplication.processEvents()
        return pages
    
    # Frees Memory for a Process
    def freeSpace(self,pages) -> None:
        for i in pages:
            self.changeTablePage(i,"lightgreen",5)
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
            else:
                self.textBox_proximo_id.setText("N/A")
                self.textBox_proximo_size.setText("0")
        #Only Changes in Remaining Time/Elapsed Time
        elif(upType == Updates.TIMER):
            self.textBox_tiempo_transcurrido.setText(str(self.elapsedTime))
            self.textBox_tiempo_restante.setText(str(self.remainingTime))
            self.textBox_quantumGlobal.setText(str(self.quantumCounter))
        #Blocked Process
        elif(upType == Updates.BLOCKED):
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
        elif(upType == Updates.END):
            self.textBox_restantes.setText(str(0))
            self.textBox_quantumGlobal.setText(str(0))
            self.tablaProcesos.clearContents()
        # Suspended Process
        elif(upType == Updates.SUSPEND):
            if(self.suspendedProcess):
                self.textBox_proximo_memoria_id.setText(str(self.suspendedProcess.getID()))
                self.textBox_proximo_memoria_size.setText(str(self.suspendedProcess.getSize()))
            else:
                self.textBox_proximo_memoria_id.setText("N/A")
                self.textBox_proximo_memoria_size.setText("")
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
    def changeTablePage(self,indx: int, color : str, progress:int):
        if(indx == 0):
            self.progressBar.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar.setValue(progress*20)
        elif(indx == 1):
            self.progressBar_1.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_1.setValue(progress*20)
        elif(indx == 2):
            self.progressBar_2.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_2.setValue(progress*20)
        elif(indx == 3):
            self.progressBar_3.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_3.setValue(progress*20)
        elif(indx == 4):
            self.progressBar_4.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_4.setValue(progress*20)
        elif(indx == 5):
            self.progressBar_5.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_5.setValue(progress*20)
        elif(indx == 6):
            self.progressBar_6.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_6.setValue(progress*20)
        elif(indx == 7):
            self.progressBar_7.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_7.setValue(progress*20)
        elif(indx == 8):
            self.progressBar_8.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_8.setValue(progress*20)
        elif(indx == 9):
            self.progressBar_9.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")  
            self.progressBar_9.setValue(progress*20)
        elif(indx == 10):
            self.progressBar_10.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_10.setValue(progress*20)
        elif(indx == 11):
            self.progressBar_11.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_11.setValue(progress*20)
        elif(indx == 12):
            self.progressBar_12.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_12.setValue(progress*20)
        elif(indx == 13):
            self.progressBar_13.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_13.setValue(progress*20)
        elif(indx == 14):
            self.progressBar_14.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_14.setValue(progress*20)
        elif(indx == 15):
            self.progressBar_15.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_15.setValue(progress*20)
        elif(indx == 16):
            self.progressBar_16.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_16.setValue(progress*20)
        elif(indx == 17):
            self.progressBar_17.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_17.setValue(progress*20)
        elif(indx == 18):
            self.progressBar_18.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_18.setValue(progress*20)
        elif(indx == 19):
            self.progressBar_19.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_19.setValue(progress*20)
        elif(indx == 20):
            self.progressBar_20.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_20.setValue(progress*20)
        elif(indx == 21):
            self.progressBar_21.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_21.setValue(progress*20)
        elif(indx == 22):
            self.progressBar_22.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_22.setValue(progress*20)
        elif(indx == 23):
            self.progressBar_23.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_23.setValue(progress*20)
        elif(indx == 24):
            self.progressBar_24.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_24.setValue(progress*20)
        elif(indx == 25):
            self.progressBar_25.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_25.setValue(progress*20)
        elif(indx == 26):
            self.progressBar_26.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_26.setValue(progress*20)
        elif(indx == 27):
            self.progressBar_27.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_27.setValue(progress*20)
        elif(indx == 28):
            self.progressBar_28.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_28.setValue(progress*20)
        elif(indx == 29):
            self.progressBar_29.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_29.setValue(progress*20)
        elif(indx == 30):
            self.progressBar_30.setStyleSheet("QProgr/essBar::chunk {background-color: " + color + ";}")
            self.progressBar_30.setValue(progress*20)
        elif(indx == 31):
            self.progressBar_31.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_31.setValue(progress*20)
        elif(indx == 32):
            self.progressBar_32.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_32.setValue(progress*20)
        elif(indx == 33):
            self.progressBar_33.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_33.setValue(progress*20)
        elif(indx == 34):
            self.progressBar_34.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_34.setValue(progress*20)
        elif(indx == 35):
            self.progressBar_35.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_35.setValue(progress*20)
        elif(indx == 36):
            self.progressBar_36.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_36.setValue(progress*20)
        elif(indx == 37):
            self.progressBar_37.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_37.setValue(progress*20)
        elif(indx == 38):
            self.progressBar_38.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_38.setValue(progress*20)
        elif(indx == 39):
            self.progressBar_39.setStyleSheet("QProgressBar::chunk {background-color: " + color + ";}")
            self.progressBar_39.setValue(progress*20)
        else:
            return