#Qt imports
from PySide6.QtWidgets import QMainWindow, QWidget
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem

#UI Imports
from view.ui_tableBCP import Ui_Form as TableBCP

#Library Imports
import keyboard
from typing import List
from models.process import Process

class BCP_table(QWidget):
    #Atributes
    pList : List[Process]
    
    # Constructor
    def __init__(self, pList:List[Process]):
        super().__init__()
        self.ui = TableBCP()
        self.ui.setupUi(self)
        self.setWindowTitle("Tabla BCP")
        # Initialize BCPTable
        if(pList != None): 
            self.pList = pList
            
        else : self.pList = list()
    
    #Insert row in Time Table
    def insertTimeRow(self,process:Process):
        n = self.ui.tableTStats.rowCount()
        stat = process.stats
        self.ui.tableTStats.insertRow(n)
        self.ui.tableTStats.setItem(n,0,QTableWidgetItem(str(process.getID())))
        self.ui.tableTStats.setItem(n,1,QTableWidgetItem(str(stat.getArrivalTime())))
        self.ui.tableTStats.setItem(n,2,QTableWidgetItem(str(stat.getEndTime())))
        self.ui.tableTStats.setItem(n,3,QTableWidgetItem(str(stat.getReturnTime())))
        self.ui.tableTStats.setItem(n,4,QTableWidgetItem(str(stat.getAnswerTime())))
        self.ui.tableTStats.setItem(n,5,QTableWidgetItem(str(stat.getWaitTime())))
        self.ui.tableTStats.setItem(n,6,QTableWidgetItem(str(stat.getServiceTime())))

    def startTable(self):
        for i in self.pList:
            self.insertTimeRow(i)