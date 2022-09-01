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
        return str(self.valueA) + self.operation + str(self.valueB) + " = " + str(self.time)
    
    def getTime(self) -> int:
        return self.time
    
    def getName(self) -> str:
        return self.programerName
    
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