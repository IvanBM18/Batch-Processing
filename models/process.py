class Process:
    # Class Atributes
    valueA : int
    valueB : int
    operation: str
    time : int
    elapsedTime : int
    processID : str
    
    # Class constructor
    def __init__(self,valueA,valueB,operation,time,processID) -> None:
        self.valueA = valueA
        self.valueB = valueB
        self.operation = operation
        self.time = time
        self.processID = processID
        self.elapsedTime = 0
        
    # Class Methods
    def setElapsedTime(self,t):
        self.elapsedTime = int(t)
    
    def toString(self):
        return str(self.valueA) + self.operation + str(self.valueB) + " = " + str(self.time)
    
    def getTime(self) -> int:
        return self.time
    
    def getElapsedTime(self) -> int:
        return self.elapsedTime
    
    def getID(self) -> str:
        return self.processID
    
    def getOperation(self) -> str:
        return self.operation
    
    def getFullOperation(self) -> str:
        return str(self.valueA) + self.operation + str(self.valueB)
    
    def getResult(self) -> int:
        if(self.operation == "+"):
            return self.valueA + self.valueB
        elif(self.operation == "-"):
            return self.valueA - self.valueB
        elif(self.operation == "*"):
            return self.valueA * self.valueB
        elif(self.operation == "/"):
            return self.valueA / self.valueB
        elif(self.operation == "%"):
            return self.valueA % self.valueB
        elif(self.operation == "^"):
            return self.valueA ** self.valueB