import random

"""
Gibt die Spielerklärung auf der Konsole wieder
"""
def startMessage():
    print("""
    42 + 7 - Spiel""")
    print("""
    Du und der Computer wählen nacheinander eine Zahl von
    1 bis 16. Die Zahlen werden aufeinander addiert. Der Spieler,
    der die 50 überschreitet, hat verloren. Durch Eingabe einer '0'
    beendest du das Spiel""")

"""
Funktion für den Zug des Spielers
"""
def playerTurn(points):
    number = int(input("Du: "))
    if (number == 0):
        return 99999
    points += number
    return points

"""
Funktion für den Zug des Computers
"""
def computerTurn(points):
    number = random.randint(1, 16)
    print("Computer: ", number)
    points += number
    return points

"""
Funktion einer Spielrunde
"""
def game():
    points = 0
    while(42):
        """
        Schleife führt den playerTurn() aus und erhöht die Gesamtpunkte (points),
        dann wird geprüft, ob 50 Punkte erreicht/überschritten wurden und das Spiel
        ggf. beendet.
        Dann wird das gleiche für den computerTurn() durchgeführt.
        """
        points = playerTurn(points)
        if (points == 99999): # prüft, ob der Spieler 0 eingegeben hat
            print("Du hast das Spiel beendet!")
            break;
        print()
        print("Summe: ", points)
        if(points >= 50): # prüft, ob der Spieler die 50 überschritten hat
            print("Du hast verloren!")
            break;

        print()
        
        points = computerTurn(points)
        print()
        print("Summe: ", points)
        if(points >= 50): # prüft, ob der Computer die 50 überschritten hat
            print("Der Computer hat verloren!")
            break;
        print("-------------------------")
        print()
       
"""
Hier beginnt das Spiel
"""
startMessage()
print()
game()
