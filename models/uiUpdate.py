from enum import Enum
class Updates(Enum):
    #No Changes
    NONE = 0
    #New Process
    NEW = 1
    #Time Update
    UPDATE = 2
    #Blocked Process
    BLOCKED = 3
    #Process Finishd
    END = 4