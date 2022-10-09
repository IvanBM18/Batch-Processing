class TimeStats:
#Class Atributes
    # Hora Llegada |
    arrival : int
    # Hora Fin |
    end : int 
    # Tiempo de respuesta (entrada a procesamiento - llegada)
    answer : int # |
    # Tiempo de retorno (Tiempo total) |
    totalReturn : int
    #Tiempo de Espera (espera para usar el procesador)
    wait : int # |
    #Tiempo de servicio |
    service : int
    
    def __init__(self) -> None:
        self.arrival = 0
        self.end = 0
        self.answer = 0
        self.totalReturn = 0
        self.wait = 0
        self.service = 0
        
# Class Methods

    def getArrivalTime(self) -> int:
        return self.arrival
    def getEndTime(self) -> int:
        return self.end
    def getAnswerTime(self) -> int:
        return self.answer
    def getReturnTime(self) -> int:
        return self.totalReturn
    def getWaitTime(self) -> int:
        return self.wait
    def getServiceTime(self) -> int:
        return self.service

    def setArrivalTime(self,t : int):
        self.arrival = t
    def setEndTime(self,t : int):
        self.end = t
    def setAnswerTime(self,t : int):
        self.answer = t
    def setReturnTime(self,t : int):
        self.totalReturn = t
    def setWaitTime(self,t : int):
        self.wait = t
    def setServiceTime(self,t : int):
        self.service = t