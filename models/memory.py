class Memory:
    PAGE_SIZE = 5 
    def __init__(self) -> None:
        self.pageList = []
        self.firstFreePage = 0
        self.freePages = 40
        
        self.pageList.extend([True for _ in range(44)])
        self.reservePage(43)
        self.reservePage(42)
        self.reservePage(41)
        self.reservePage(40)
        
    def reservePage(self,index : int):
        self.pageList[index] = False
        self.freePages -= 1
        self._findFirstFreePage()
    
    def freePage(self,index : int):
        self.pageList[index] = True
        
    def getFirstFreePage(self) -> int:
        return self.firstFreePage
    
    def getLastFreePage(self) -> int:
        return self.lastFreePage
    
    def reserveMemory(self,size : int) -> list:
        pages = []
        while size > 0:
            pages.append(self.firstFreePage)
            self.reservePage(self.firstFreePage)
            size -= self.PAGE_SIZE
            # No hay memoria suficiente
            if(size and self.freePages == 0):
                self.freeMemory(pages)
                return None   
        return pages
    
    def freeMemory(self,pages : list):
        for page in pages:
            self.freePage(page)
        self._findFirstFreePage()
    
    def _findFirstFreePage(self):
        self.firstFreePage = 0
        while(not self.pageList[self.firstFreePage]):
            self.firstFreePage += 1