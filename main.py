from KeinePremiumLampe import KeinePremiumLampe
from PremiumLampe import PremiumLampe

if __name__ == "__main__":
    #Sehr zeitaufwändig -> 20sek

    #Eine Lampe für die Küche
    nichtPremiumLampe1 = KeinePremiumLampe("Küche")

    #Eine fürs Wohnzimmer
    nichtPremiumLampe2 = KeinePremiumLampe("Wohnzimmer")

    #Viel schneller -> 10sek
    #Eine Lampe für die Küche
    permiumLampe1 = PremiumLampe("Küche")

    #Eine fürs Wohnzimmer
    permiumLampe2 = permiumLampe1.clone()
    permiumLampe2.setZimmer("Wohnzimmer")
