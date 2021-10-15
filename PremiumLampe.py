from Lampe import Lampe
from Prototyp import Prototyp
import copy

class PremiumLampe(Prototyp, Lampe):
    """Test instanciation of PremiumLampe.

    >>> type(PremiumLampe("TestZimmer"))
    <class 'PremiumLampe.PremiumLampe'>

    Test getZimmer() of PremiumLampe.

    >>> (PremiumLampe("TestZimmer")).getZimmer()
    'TestZimmer'

    Test setZimmer() of PremiumLampe.
    >>> PremiumLampe("TestZimmer").setZimmer("TestZimmerNeu")

    Test an() of PremiumLampe.
    >>> PremiumLampe("TestZimmer").an()
    Premium An

    Test aus() of PremiumLampe.
    >>> PremiumLampe("TestZimmer").aus()
    Premium Aus
    """
    def clone(self):
        return copy.deepcopy(self)

    def an(self):
        print("Premium An")

    def aus(self):
        print("Premium Aus")