from Lampe import Lampe

class KeinePremiumLampe(Lampe):
    """Test instanciation of KeinePremiumLampe.

    >>> type(KeinePremiumLampe("TestZimmer"))
    <class 'KeinePremiumLampe.KeinePremiumLampe'>

    Test getZimmer() of KeinePremiumLampe.

    >>> (KeinePremiumLampe("TestZimmer")).getZimmer()
    'TestZimmer'

    Test setZimmer() of KeinePremiumLampe.
    >>> KeinePremiumLampe("TestZimmer").setZimmer("TestZimmerNeu")

    Test an() of KeinePremiumLampe.
    >>> KeinePremiumLampe("TestZimmer").an()
    An

    Test aus() of KeinePremiumLampe.
    >>> KeinePremiumLampe("TestZimmer").aus()
    Aus
    """
    def an(self):
        print("An")

    def aus(self):
        print("Aus")