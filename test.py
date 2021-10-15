import KeinePremiumLampe
import PremiumLampe

def test():
    import doctest
    # doctest.IGNORE_EXCEPTION_DETAIL
    doctest.testmod(KeinePremiumLampe)
    doctest.testmod(PremiumLampe)
    print("just test doctest")

if __name__ == "__main__":
    test()
