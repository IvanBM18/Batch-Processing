#Qt imports
from PySide6.QtWidgets import QMainWindow, QWidget
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem

#UI Imports
from view.ui_tableBCP import Ui_Form as TableBCP

#Library Imports
import keyboard

class BCP_table(QWidget):
    
    # Constructor
    def __init__(self):
        super().__init__()
        self.ui = TableBCP()
        self.ui.setupUi(self)
        self.setWindowTitle("Tabla BCP")
    
    
