from models.process import Process
# Clase que maneja la lista de usuarios suspendidos
class SuspendManager():
    FILE_NAME = "suspended.txt"
    def __init__(self):
        self._suspendedList = [Process]
        self._file = open(self.FILE_NAME,"w")
        self._file.write("--- Suspended Processes ---\n")
        self._processOnTop = None
        self._closeFile()
        
    def _openOnWrite(self):
        self._file = open(self.FILE_NAME,"w")
        self._file.write("--- Suspended Processes ---\n")
        
    def _openOnAppend(self):
        self._file = open(self.FILE_NAME,"a")
        
    def _closeFile(self):
        self._file.close()
        
    def isEmpty(self):
        return len(self._suspendedList) == 0
        
    def getProcessOnTop(self):
        return self._processOnTop if self._processOnTop else None
        
    def addProcess(self,process):
        if(not self._processOnTop):
            self._processOnTop = process
        self._suspendedList.append(process)
        self.processToFile(process)
    
    def retrieveProcess(self):
        if(len(self._suspendedList) > 0):
            auxProcess = self._processOnTop
            self._processOnTop = self._suspendedList.pop(0)
            # Updates the file
            self._openOnWrite()
            for i in self._suspendedList:
                self._file.write(i.toFile())
            self._closeFile()
            return auxProcess
        return None
        
    def processToFile(self,process : Process):
        self._openOnAppend()
        self._file.write(process.toFile())
        self._closeFile()