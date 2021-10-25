import random

"""
Funktion für den Spielerzug
"""
def playerTurn():
    return int(input("Du: "))

"""
Funktion für den Computerzug
"""
def computerTurn():
    return random.randint(1, 16)

"""
Funktion für den Spielablauf
"""
def game():
    points = 0
    weiter = True
    while(weiter == True):
        """
        Unendliche While-Schleife. Sie wird nur durch breaks durchbrochen
        """
        correct = False
        while(correct != True):
            """
            Prüft, ob die Eingabe des Spielers korrekt ist
            """
            playerNumber = playerTurn()
            if (playerNumber == 0):
                print("Spiel beendet!")
                break;
            elif (playerNumber < 0 or playerNumber > 16):
                print("Falsche Eingabe!")
                correct = False
            else:
                correct = True
            
        points += playerNumber

        if (points >=50):
            print("Summe: ", points)
            print("Du hast verloren!")
            break;

        print("Summe: ", points)
        
        computerNumber = computerTurn()
        
        print("Computer: ", computerNumber)

        points += computerNumber

        if (points >= 50):
            print("Summe: ", points)
            print("Computer hat verloren!")
            break;

        print("Summe: ", points)
        print()

"""
Hier findet das Spiel statt
"""
i = 0
anzahlRunden = int(input("Anzahl Runden: "))
while(i < anzahlRunden):
    game()
    i += 1
