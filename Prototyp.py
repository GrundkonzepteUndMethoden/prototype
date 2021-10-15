from abc import abstractmethod, ABC

class Prototyp(ABC):
    @abstractmethod
    def clone(self):
        pass