class Batch:
    #Class Atributes
    processList = []
    remainingProcess : int
    
    #Constructor
    def __init__(self) -> None:
        self.remainingProcess = 0
        self.processList = list()
        
    #Class Methods
    def addProcess(self,process):
        self.processList.append(process)
        self.remainingProcess += 1
    
    def getProcess(self,indx):
        return self.processList[indx]

    def getTopProcess(self):
        return self.processList[0]
    
    def getProcessList(self):
        return self.processList
    
    def getRemainingProcess(self):
        return self.remainingProcess
    
    def removeProcess(self):
        self.processList.pop(0)
        self.remainingProcess -= 1