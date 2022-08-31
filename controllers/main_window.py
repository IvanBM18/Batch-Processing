#Validaciones
#Division por 0
import time
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QMessageBox

from view.mainwindow import MainWindow
from models.queue import Queue
from models.process import Process

class MainForm(QMainWindow, MainWindow):
    #Atributtes
    totalProcess : int = 0
    counter : int = 0
    name : str = ""
    operation : str = "+"
    queue = Queue()
    
    #Constructor
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.name = "Ivan"
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
    #Inhabilitar esto si lo demas esta en 0
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
    
    #Checar esto no sirve al 100
    def processBatches(self):
        if(self.totalProcess != 0):
            print(self.queue.toString())
            
        
        # indx = 0
        # self.counter = 0
        # auxCont = 0
        # self.plainTextEdit_Counter.setText(str(self.counter))
        # auxVal = self.queue.getFront()
        # while(indx < self.totalProcess):
        #     if(auxCont >= auxVal.getTime()):
        #         auxCont = 1
        #         self.queue.dequeue()
        #         auxVal = self.queue.getFront()
        #         indx +=1
        #     else:
        #         auxCont += 1
        #     time.sleep(1)
        #     self.counter += 1
        #     self.plainTextEdit_Counter.setText(str(self.counter))
        #     #self.plainTextEdit_PendingBatch.setText(str(self.totalProcess - indx))
        #     self.counter += 1
        # print("[INFO] Procesos terminados")