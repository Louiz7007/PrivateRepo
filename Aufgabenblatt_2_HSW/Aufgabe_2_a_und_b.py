# Aufgabe 2: Berechnung Volumen Pyramide in Ellen
# Umrechnung in Kubikmeter
# Ausgabe beider Ergebnisse
# Zusätzlich: Ausgabe benötigter Sandsteinblöcke

grundflaeche = 440 * 440;
hoehe = 280;
volumenEllen = (1/3) * grundflaeche * hoehe;
print("Das Volumen beträgt ", volumenEllen, " Ellen.");
grundFlaecheMeter = (440 * 0.52) * (440 * 0.52);
hoeheMeter = 280 * 0.52;
volumenMeter = (1/3) * grundFlaecheMeter * hoeheMeter;
print("Das Volumen beträgt ", volumenMeter, " Kubikmeter.");
