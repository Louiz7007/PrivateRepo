# Aufgabe 2: Berechnung Volumen Pyramide in Ellen
# Umrechnung in Kubikmeter
# Umrechnung in römische Scheffel ! nicht gefunden !
# Ausgabe beider Ergebnisse
# Zusätzlich: Ausgabe benötigter Sandsteinblöcke

grundflaeche = 440 * 440;
hoehe = 280;
volumenEllen = (1/3) * grundflaeche * hoehe;
print("Das Volumen beträgt ", "%10.2f" % volumenEllen, " Ellen.");
grundFlaecheMeter = (440 * 0.52) * (440 * 0.52);
hoeheMeter = 280 * 0.52;
volumenMeter = (1/3) * grundFlaecheMeter * hoeheMeter;
print("Das Volumen beträgt ", "%10.2f" % volumenMeter, " Kubikmeter.");
volumenBlock = 2 * 2 * 2;
anzahlBenoetigterBloecke = volumenEllen / volumenBlock;
print("Das entspricht ", "%10.2f" % anzahlBenoetigterBloecke, " Steinblöcke!");
print("Hinweis: Alle Ergebnisse wurden auf zwei Nachkommastellen gekürzt.");
