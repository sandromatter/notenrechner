#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""notenrechner.py: Super simple command line python script to calculate average grades (CH)."""

__author__      = "Sandro Matter, Tino Dietrich"
__copyright__   = "Copyright 2020"
__license__     = "GPL"
__version__     = "3.0"


notenliste = {}


# Abfrage des Faches.
def fach_abfragen():
    fach_eingabe_string = "\nVon welchem Fach möchten Sie die Noten berechnen? "
    fach_eingabe = str(input(fach_eingabe_string))
    fach_eingabe = fach_eingabe.capitalize()

    # Prüft ob das Fach bereits erfasst wurde.
    if fach_eingabe in notenliste:
        print("\nAchtung! Sie haben dieses Fach bereits erfasst.")
        fach_eingabe_bestaetigung_string = f"Geben Sie '{fach_eingabe}' nochmals ein, um den Notenschnitt für das bestehende Fach zu löschen und neu zu erfassen oder 'x' um abzubrechen: "
        abfrage_fach = str(input(fach_eingabe_bestaetigung_string))

        while True:
            if abfrage_fach != "x" and abfrage_fach != f"{fach_eingabe}":
                abfrage_fach = input("Ungültige Eingabe.\n" + fach_eingabe_bestaetigung_string)

            elif abfrage_fach == "x":
                break

            elif abfrage_fach == fach_eingabe:
                return fach_eingabe

    else:
        return fach_eingabe


# Notenschnitt eines einzelnen Faches berechnen.
def notenschnitt_berechnen():
    noten = []
    counter = 0
    note_abfrage_string = "Geben Sie Ihre Note (1-6) ein oder 'x' um abzubrechen: "

    while True:
        note_abfrage = input(note_abfrage_string)
        
        # Unterbricht das Nachfragen nach weiteren Noten.
        if note_abfrage == "x": 
            if counter > 0:
                break
            
            else:
                print("Bitte geben Sie mindestens eine Note ein.")

        # Prüft auf ungültige Usereingaben.
        else:
            try:
                note_float = float(note_abfrage)

                if note_float >= 1.0 and note_float <= 6.0:
                    noten.append(note_float)
                    counter += 1

                else:
                    print("Ungültige Eingabe. ")

            except ValueError:
                print("Ungültige Eingabe. ")

    notensumme = sum(noten)
    notenschnitt = notensumme / counter

    return notenschnitt


# Gibt erfassten Notenschnitt des Faches nach Abbruch durch 'x' aus.
# Listet Notenschnitte in Dictionary nach Fach und Schnitt.
def notenschnitte_auflisten():
    fach = fach_abfragen()

    # Fügt neues Fach und Notenschnitt zur Notenliste.
    if fach != None:
        notenschnitt = notenschnitt_berechnen()
        print(f"\nIhr Notenschnitt für das Fach {fach} ist {notenschnitt:.2f}.\n")
        notenliste[str(fach)] = float(notenschnitt)


# Main Programm, fragt beim User nach weiterer Eingabe.
def main():
    notenschnitte_auflisten()
    fach_eingabe_weitere_string = "Möchten Sie eine weiteres Fach erfassen?\nBitte mit 'y' für Yes/Ja oder 'n' für No/Nein antworten: "
    fach_eingabe_weitere = input(fach_eingabe_weitere_string)

    # Checkt ob weitere Eingabe gewünscht ist bis User mit 'Nein' abbricht.
    while True:
        if fach_eingabe_weitere != "y" and fach_eingabe_weitere != "n":
            fach_eingabe_weitere = input("Ungültige Eingabe.\n" + fach_eingabe_weitere_string)
        
        elif fach_eingabe_weitere == "y":
            notenschnitte_auflisten()
            fach_eingabe_weitere = input(fach_eingabe_weitere_string)
        
        elif fach_eingabe_weitere == "n":
            break
    
    notensumme_gesamt = sum(notenliste.values())
    notenschnitt_gesamt = notensumme_gesamt / len(notenliste)

    print("\n------------------------------------------------")
    print(f"\nIhr Gesamtnotenschnitt beträgt {notenschnitt_gesamt:.2f}.\n")
    print("------------------------------------------------\n")
    print("Dies sind die Durchschnitte Ihrer Fächer:\n")
        
    for i in notenliste : 
        print(f"{i}:\t\t\t{notenliste[i]:.2f}")

    print(f"\n------------------------------------------------")


if __name__ == "__main__":
    main()
