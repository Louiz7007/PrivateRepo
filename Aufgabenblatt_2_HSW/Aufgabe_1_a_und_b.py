menge = input("Getankte Benzinmenge in Litern: ");
bruttoPreisLiter = input("Preis je Liter (EUR): ");
bruttoPreisGesamt = float(menge) * float(bruttoPreisLiter);
print("Getankte Liter: ", menge);
print("Preis pro Liter: ", bruttoPreisLiter);
print("Gesamtbetrag Tankfüllung: ", bruttoPreisGesamt);
