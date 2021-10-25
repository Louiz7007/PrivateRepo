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
def playerTurn():
    number = int(input("Du: "))
    return number

"""
Funktion für den Zug des Computers
"""
def computerTurn():
    number = random.randint(1, 16)
    print("Computer: ", number)
    return number

"""
Funktion einer Spielrunde
"""
def game():
    points = 0
    correct = False
    while(42):
        while(not correct):
            playerNumber = playerTurn()
            if (playerNumber == 0):
                print("Du hast das Spiel beendet!")
                end = True;
            elif (playerNumber >= 1 or playerNumber <= 16):
                correct = True
        points += playerNumber
        correct = False
        if (points >= 50):
            print("Du hast verloren!")
            break;
        print("Summe: ", points)
        print()

        points += computerTurn()
        if (points >= 50):
            print("Computer hat verloren!")
            break;
        print("Summe: ", points)
        print()
        
"""
Hier beginnt das Spiel
"""
startMessage()
print()
game()





























