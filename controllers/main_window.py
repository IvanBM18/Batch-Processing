#Validaciones
#Division por 0
import queue
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
        self.tabWidget.setCurrentIndex(0)
        self.plainTextEdit_capturedProcess.setReadOnly(True)
        self.pushButton_aceptProcess.clicked.connect(self.setTotalProcess)
        self.pushButton_addProcess.clicked.connect(self.newProcess)
        self.plainTextEdit_name.textChanged.connect(self.setName)
        self.plainTextEdit_operationFirst.textChanged.connect(self.setOperationFirst)
        self.plainTextEdit_operationSecond.textChanged.connect(self.setOperationSecond)
        self.plainTextEdit_SetTime.textChanged.connect(self.setTime)
        self.plainTextEdit_setID.textChanged.connect(self.setID)
    
    #Setters
    def setTotalProcess(self):
        validateEntry = self.plainTextEdit_process.toPlainText()
        if (str(validateEntry).isdigit() == False or int(validateEntry) < 1):
            print("[ERROR] introduce un numero")
            self.plainTextEdit_process.setPlainText("")
            msgBox = QMessageBox()
            msgBox.setText("Introduce un numero mayor a 0")
            msgBox.setWindowTitle("ERROR")
            msgBox.exec_()
        self.totalProcess = int(validateEntry)
        self.plainTextEdit_process.setPlainText(validateEntry)
        self.plainTextEdit_process.setEnabled(False)
        self.pushButton_aceptProcess.setEnabled(False)
        
    def setName(self):
        self.name = self.plainTextEdit_name.toPlainText()
        
    def setOperationFirst(self):
        validateEntry = self.plainTextEdit_operationFirst.toPlainText()
        if (str(validateEntry).isdigit() == False and validateEntry != ""):
            print("[ERROR] introduce un numero")
            msgBox = QMessageBox()
            msgBox.setText("Introduce un numero mayor a 0")
            msgBox.setWindowTitle("ERROR en valores de operación")
            msgBox.exec_()
            self.plainTextEdit_operationFirst.setPlainText("")
            
    def setOperationSecond(self):
        validateEntry = self.plainTextEdit_operationSecond.toPlainText()
        if (str(validateEntry).isdigit() == False and validateEntry != ""):
            print("[ERROR] introduce un numero")
            msgBox = QMessageBox()
            msgBox.setText("Introduce un numero mayor a 0")
            msgBox.setWindowTitle("ERROR en valores de Operación")
            msgBox.exec_()
            self.plainTextEdit_operationSecond.setPlainText("")
    
    def setTime(self):
        validateEntry = self.plainTextEdit_SetTime.toPlainText()
        if ((str(validateEntry).isdigit() == False or int(validateEntry) < 1) and validateEntry != ""):
            print("[ERROR] introduce un numero")
            msgBox = QMessageBox()
            msgBox.setText("Introduce un numero mayor a 0")
            msgBox.setWindowTitle("ERROR en Tiempo")
            msgBox.exec_()
            self.plainTextEdit_SetTime.setPlainText("")
    
    def setID(self):
        validateEntry = self.plainTextEdit_setID.toPlainText()
        if (str(validateEntry).isdigit() == False and validateEntry != ""):
            print("[ERROR] introduce un numero")
            msgBox = QMessageBox()
            msgBox.setText("Introduce un numero")
            msgBox.setWindowTitle("ERROR en ID")
            msgBox.exec_()
            self.plainTextEdit_setID.setPlainText("")
    
    #Methods
    def newProcess(self):
        if(self.totalProcess == 0):
            msgBox = QMessageBox()
            msgBox.setText("Introduzca el numero total de procesos")
            msgBox.setWindowTitle("ERROR")
            msgBox.exec_()
        else:
            operation  = self.comboBox_operation.currentText()
            if(operation == "/"):
                if(int(self.plainTextEdit_operationSecond.toPlainText()) == 0):
                    msgBox = QMessageBox()
                    msgBox.setText("Introduce un numero mayor a 0")
                    msgBox.setWindowTitle("ERROR en valores de operación")
                    msgBox.exec_()
                    self.plainTextEdit_operationSecond.setPlainText("")
            self.operation = operation
            aux = Process(self.name,self.plainTextEdit_operationFirst.toPlainText(),self.plainTextEdit_operationSecond.toPlainText(),operation,self.plainTextEdit_SetTime.toPlainText(),self.plainTextEdit_setID.toPlainText())
            self.queue.enqueue(aux)
            self.counter += 1
            self.plainTextEdit_capturedProcess.setPlainText(str(self.counter))
            self.plainTextEdit_setID.setPlainText(str(int(self.plainTextEdit_setID.toPlainText())+1))
        self.plainTextEdit_operationFirst.setPlainText("")
        self.plainTextEdit_operationSecond.setPlainText("")
        self.plainTextEdit_SetTime.setPlainText("")
        if(self.counter == self.totalProcess and self.totalProcess != 0):
            currentIndx = self.tabWidget.currentIndex()
            self.tabWidget.setCurrentIndex(currentIndx + 1)
            print(self.queue.toString())
            self.processBatches()
    
    def proceessBatches(self):
        pass