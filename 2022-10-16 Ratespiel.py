# Ratespiel
#
# In diesem Spiel gibt es eine Geheime Zahl. Der Spieler muss diese Zahl in mehreren Schritten
# erraten. Um dem Ziel näher zu kommen, WIRD dem Spieler der Hinweis gegeben, ob sein Tipp zu hoch
# oder zu niedrig war. Wenn der Spieler die geheime Zahl erraten hat, wird der Spieler gebührened gefeiert.

import random
from datetime import datetime
import os
os.system('cls')

#
# Variablendefinition
# 
class User:
    name: str
    versuche = 999
    speicherdatum: str
    
bestenliste = []
zufallszahl: int
mainschleife = True
user = User()
user.versuche = 0

def teste(Wert):
    try:
        Wert = int(Wert)
    except Exception:
        return False
    return Wert 

def save_spielerstand(versucheuebergabe):
    # spielerstand={"name": Thomas   , "versuche": 12      , "Gespeichert am": "18-10-2022 12:48"}
    user.speicherdatum = datetime.now()
    spielerstand = {"name": user.name, "versuche": versucheuebergabe, "Gespeichert am": user.speicherdatum}
    bestenliste.append(spielerstand)

def schreiben_bestenliste():
    bestendatei = open("Bestendatei.txt","w+")
    bestendatei.write(bestenliste)
    bestendatei.close()

def lesen_bestenliste():
    bestendatei = open("Bestendatei.txt","r+")
    b = bestendatei.read()
    bestendatei.close()
    return b

def weiterspielen():
    """
    Frage nach weiter J/N
    """
    schleife = True
    while schleife:
        restart_game = input("Nochmal? (j/n): ")
        if restart_game == "j":
            return True
        elif restart_game == "n":
            print("Okay, Tschau.")
            return False
        else: 
            continue

def wuerfel():
    a = random.randint(1, 30)
    return a

print("-------------------------------------------------------------------------------")
print(" Hier ist ein kleines Spiel für Dich.")
print(" Ich habe eine kleine ganzzahlige Zahl zwischen 1 und 30 die Du erraten sollst.")
print("-------------------------------------------------------------------------------")
zufallszahl = wuerfel()
user.name = input("Bitte sag mir deinen Namen: ")
while mainschleife:
    user_zahl = 0
    user_zahl = input ( "Bitte gib eine Zahl zwischen 1 und 30 ein: " )
    user_zahl = teste(user_zahl)
    user.versuche = user.versuche + 1

    if user_zahl == False:
        print("Deine Eingabe ist keine ganzzahlige Zahl")
        continue
    elif  user_zahl  <  zufallszahl :
        print("Dein Tipp ist leider zu niedrig.")
    elif  user_zahl  >  zufallszahl :
        print("Dein Tipp ist leider zu hoch.")
    elif  user_zahl  ==  zufallszahl :
        print("🎉 🎉 🎉 Gewonnen! 🎉 🎉 🎉")
        print(f"Du hast insgesamt {user.versuche} Versuche gehabt.")
        if weiterspielen():
           zufallszahl = wuerfel()
           user.versuche = 0
           continue
        else:
            break

hochstand = lesen_bestenliste()
print("-------------------------------------------------------------------------------")
print(f"High-Score war beim letzten mal war {hochstand} ")

if int(hochstand) < user.versuche :
    print(f"Leider bist du {user.versuche - hochstand} Versuche schlechter")
elif int(hochstand) > user.versuche :
    print(f"Wow du bist {hochstand- user.versuche} Versuche besser")
    save_spielerstand(user.versuche)
    schreiben_bestenliste()
else:
    print(f"Keine Veränderung am High-Score. Schade.")

print("-------------------------------------------------------------------------------")

