from abc import abstractmethod, ABC
import time

class Lampe(ABC):
    """
        Hier passiert ein Zeitaufwändiges Setup vom Hersteller
    """
    def __init__(self, zimmer):
        time.sleep(10)
        self.zimmer = zimmer
    
    def setZimmer(self, zimmer):
        self.zimmer = zimmer
    
    def getZimmer():
        return self.zimmer

    @abstractmethod
    def an():
        pass

    @abstractmethod
    def aus():
        pass