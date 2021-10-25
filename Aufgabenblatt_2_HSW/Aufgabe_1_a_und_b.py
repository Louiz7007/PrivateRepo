# Aufgabe 1: Eingabe getankte Benzinmenge, Eingabe Brutto Preis pro Liter
# Ausgabe Getankte Liter, Ausgabe Preis pro Liter, Ausgabe Gesamtpreis Brutto, Ausgabe Gesamtpreis Netto

menge = input("Getankte Benzinmenge in Litern: ")
bruttoPreisLiter = input("Preis je Liter (EUR): ")
bruttoPreisGesamt = float(menge) * float(bruttoPreisLiter)
print("Getankte Liter: ", menge)
print("Preis pro Liter: ", bruttoPreisLiter)
print("Gesamtbetrag Tankfüllung (Brutto): ", bruttoPreisGesamt)
print("Mehrwertsteuer bei Benzin: 24,74 %")
nettoPreisGesamt = bruttoPreisGesamt / 1.2474
print("Gesamtbetrag Tankfüllung (Netto): ", "%4.4f" % nettoPreisGesamt)
