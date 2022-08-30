from unittest import result


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
    
    # Class Methods
    def enqueue(self,value) -> None | int:
        self.end += 1
        self.values.append(value)
        return self.end
    
    def dequeue(self):
        if(self.isEmpty() != True):
            index = int(self.front)
            self.front += 1
            return self.values[index]
    
    def isEmpty(self) -> bool:
        if((self.front == 0 and self.end == self.front -1)):
            return True
        return False

    def getFront(self):
        if(self.isEmpty() != True):
            return self.values[self.front]
    
    def getLength(self):
        return self.end - self.front + 1
    
    def toString(self):
        result = ""
        for i in self.values:
            result += i.toString() + " "
        return result