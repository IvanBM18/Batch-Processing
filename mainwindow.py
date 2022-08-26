from PySide2.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        #super llama al constructor para crear la ventana
        super(MainWindow,self).__init__()
        ui = Ui_MainWindow()
        #metodo para meter los elementos de la vista
        ui.setupUi(self) #le ponemos self para mandarle lo que se necesite