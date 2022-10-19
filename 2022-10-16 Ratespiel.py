# Ratespiel
#
# In diesem Spiel gibt es eine Geheime Zahl. Der Spieler muss diese Zahl in mehreren Schritten
# erraten. Um dem Ziel näher zu kommen, WIRD dem Spieler der Hinweis gegeben, ob sein Tipp zu hoch
# oder zu niedrig war. Wenn der Spieler die geheime Zahl erraten hat, wird der Spieler gebührened gefeiert.

import random
from datetime import datetime
import os
os.system('cls')

def teste(Wert):
    try:
        Wert = int(Wert)
    except Exception:
        return False
    return Wert 

def save_spielerstand(versuche):
    # spielerstand={"name": Thomas   , "versuche": 12      , "Gespeichert am": "18-10-2022 12:48"}
    spielerstand = {"name": user_name, "versuche": versuche, "Gespeichert am": datetime.now()}
    bestenliste.append(spielerstand)

def holezahl(wert_zahl):
    wert_zahl  = input ( "Bitte gib eine Zahl zwischen 1 und 30 ein: " )
    wert_zahl = teste(wert_zahl)
    return wert_zahl

def weiterspielen():
    """
    This function asks the user whether he/she wants to play again.
    """
    restart_game = input("Nochmal? (y/n): ")
    if restart_game == "y":
        return True
    else: 
        print("Okay, Tschau.")
        return False

def schreiben_bestenliste():
    bestendatei = open("Bestendatei.txt","w+")
    bestendatei.write(bestenliste[])
    bestendatei.close()

def lesen_bestenliste():
    bestendatei = open("Bestendatei.txt","r+")
    b = bestendatei.read()
    bestendatei.close()
    return b

def wuerfel():
    a = random.randint(1, 30)
    return a

zufallszahl = wuerfel()
mainschleife = True
versuche = 0
bestenliste = []

print("-------------------------------------------------------------------------------")
print(" Hier ist ein kleines Spiel für Dich.")
print(" Ich habe eine kleine ganzzahlige Zahl zwischen 1 und 30 die Du erraten sollst.")
print("-------------------------------------------------------------------------------")
user_name = input("Bitte sag mir deinen Namen: ")
while mainschleife:
    user_zahl = 0
    user_zahl  = input ( "Bitte gib eine Zahl zwischen 1 und 30 ein: " )
    user_zahl = teste(user_zahl)
    versuche = versuche + 1

    if user_zahl == False:
        print("Deine Eingabe ist keine ganzzahlige Zahl")
        continue
    elif  user_zahl  <  zufallszahl :
        print("Dein Tipp ist leider zu niedrig.")
    elif  user_zahl  >  zufallszahl :
        print("Dein Tipp ist leider zu hoch.")
    elif  user_zahl  ==  zufallszahl :
        print("🎉 🎉 🎉 Gewonnen! 🎉 🎉 🎉")
        print(f"Du hast insgesamt {versuche} Versuche gehabt.")
        save_spielerstand(versuche)
        if weiterspielen():
           zufallszahl = wuerfel()
           versuche = versuche + 1
           continue
        else:
            break

print("-------------------------------------------------------------------------------")
print(f"High-Score war beim letzten mal war {lesen_bestenliste()} ")
print("-------------------------------------------------------------------------------")
schreiben_bestenliste()
