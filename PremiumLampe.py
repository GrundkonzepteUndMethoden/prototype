from Lampe import Lampe
from Prototyp import Prototyp

class PremiumLampe(Prototyp, Lampe):
    def clone(self):
        return copy.deepcopy(self)

    def an():
        print("Premium An")

    def aus():
        print("Premium Aus")