class TimeStats:
#Class Atributes
    # Hora Llegada
    arrival : int
    # Hora Fin
    end : int 
    # Tiempo de respuesta (entrada a procesamiento - llegada)
    answer : int 
    # Tiempo de retorno (Tiempo total)
    totalReturn : int
    #Tiempo de Espera (espera para usar el procesador)
    wait : int
    
    def __init__(self) -> None:
        self.arrival = 0
        self.end = 0
        self.answer = 0
        self.totalReturn = 0
        self.wait = 0
        
# Class Methods

    def getArrivalTime(self) -> int:
        return self.arrival
    def getEndTime(self) -> int:
        return self.end
    def getAnswerTime(self) -> int:
        return self.answer
    def getTotalReturnTime(self) -> int:
        return self.totalReturn
    def getWaitTime(self) -> int:
        return self.wait