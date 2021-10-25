gewicht = float(input("Gewicht in Kg: "))
groesse = float(input("Größe in m: "))
print()
bmx = gewicht / (groesse ** 2)

while (bmx > 25):
    print("Ihr BMI: ", "%2.2f" % bmx)
    print()
    antwort = input("Möchten Sie Ihr Gewicht oder Ihre Größe ändern? (gew / gr) ")
    print()
    if (antwort == "gew"):
        gewicht = float(input("Neues Gewicht in Kg: "))
        print()
    elif (antwort == "gr"):
        groesse = float(input("Neue Größe in m: "))
        print()
    else:
        print("Falsche Eingabe! Bitte nur 'gew' oder 'gr' eingeben!")
    bmx = gewicht / (groesse ** 2)
print()
print("Glückwunsch, jetzt leben Sie gesund!")
print("Ihr BMI: ", "%2.2f" % bmx)
