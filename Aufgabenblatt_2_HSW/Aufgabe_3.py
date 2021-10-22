anzahlEinzelStuecke = int(input("Anzahl Einzelstücke N: "));

anzahlGros = anzahlEinzelStuecke // 144;
rest = anzahlEinzelStuecke % 144;

anzahlSchock = rest // 60;
rest = rest % 60;

anzahlDutzend = rest // 12;
rest = rest % 12;

anzahlStueck = rest;

print("Anzahl Einzelstücke N: ", anzahlEinzelStuecke);
print("Anzahl Gros: ", anzahlGros);
print("Anzahl Schock: ", anzahlSchock);
print("Anzahl Dutzend: ", anzahlDutzend);
print("Anzahl Stück: ", anzahlStueck);

