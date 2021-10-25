import random

def startMessage():
    print("""
    42 + 7 - Spiel""")
    print("""
    Du und der Computer wählen nacheinander eine Zahl von
    1 bis 16. Die Zahlen werden aufeinander addiert. Der Spieler,
    der die 50 überschreitet, hat verloren. Durch Eingabe einer '0'
    beendest du das Spiel""")

def computerZug():
    zahl = random.randint(1, 16)
    print("Computer: ", zahl)
    return zahl

def spielerZug():
    return int(input("Du: "))

def sum(spielerZahl, computerZahl):
    return spielerZahl + computerZahl

def gameRound(zwischenstand):
    spielerZahl = spielerZug()
    if (zwischenstand + spielerZahl >= 50):
        print("Du hast verloren!")
        end = True;
    computerZahl = computerZug()
    if (zwischenstand + computerZahl >= 50):
        print("Computer hat verloren!")
        end = True;
    if (not end):
        totalSum = zwischenstand + sum(spielerZahl, computerZahl)
        print("Summe: ", totalSum)
        return totalSum
    else:
        

startMessage()
print()
zwischenstand = 0;

while(zwischenstand < 50):
    zwischenstand = gameRound(zwischenstand)

    
