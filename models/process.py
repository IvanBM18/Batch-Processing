class Process:
    # Class Atributes
    programerName : str
    valueA : int
    valueB : int
    operation: str
    time : int
    processID : str
    
    # Class constructor
    def __init__(self,programmerName,valueA,valueB,operation,time,processID) -> None:
        self.programerName = programmerName
        self.valueA = valueA
        self.valueB = valueB
        self.operation = operation
        self.time = time
        self.processID = processID
        
    # Class Methods
    def toString(self):
        return str(self.valueA) + self.operation + str(self.valueB)
    
    def getTime(self) -> int:
        return self.time