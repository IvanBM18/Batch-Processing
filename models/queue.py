class Queue:
    #Class Atributes
    front : int = 0
    end : int = -1
    values = []
    
    # Class Constructor
    def __init__(self) -> None:
        self.front = 0
        self.end = -1
        self.values = []
        self.length = 0
    
    # Class Methods
    def enqueue(self,value) -> None | int:
        self.end += 1
        self.length += 1
        self.values.append(value)
        return self.end
    
    def dequeue(self):
        if(self.isEmpty() != True):
            index = int(self.front)
            self.front += 1
            self.length -= 1
            return self.values[index]
    
    def isEmpty(self) -> bool:
        if(self.length == 0):
            return True
        return False

    def getFront(self):
        if(not self.isEmpty() ):
            return self.values[self.front]
    
    def getLength(self):
        return self.length
    
    def toString(self):
        result = ""
        for i in self.values:
            result += i.toString() + " "
        return result
    
    def getBatch(self,index) -> list:
        aux = []
        for i in range(index,index +3):
            if( i < len(self.values)):
                aux.append(self.values[i])
        return aux
    
    def getList(self) -> list:
        result = []
        indx = 0
        for i in self.values:
            if (indx >= self.front):
                result.append(i)
            indx += 1
        return result