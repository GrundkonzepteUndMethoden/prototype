from Lampe import Lampe

class KeinePremiumLampe(Lampe):
    """Test instanciation of KeinePremiumLampe.

    >>> type(KeinePremiumLampe("TestZimmer"))
    <class 'KeinePremiumLampe.KeinePremiumLampe'>

    Test instanciation of KeinePremiumLampe.

    >>> (KeinePremiumLampe("TestZimmer")).getZimmer()
    'TestZimmer'

    """
    def an():
        print("An")

    def aus():
        print("Aus")