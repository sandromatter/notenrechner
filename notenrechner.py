notenliste = {}

# Abfrage des Faches
def fach_abfragen():
    fach_eingabe = str(input("\nVon welchem Fach möchten Sie die Noten berechnen? "))
    fach_eingabe = fach_eingabe.capitalize()

    return fach_eingabe

# Notenschnitt eines einzelnen Faches berechnen und prüfen auf unerlaubte Eingaben.
def notenschnitt_berechnen():
    noten = []
    counter = 0
    question_data = "Geben Sie Ihre Note (1-6) ein oder x um abzubrechen: "

    while True:
        note_input = input(question_data)
        
        # Unterbricht das Nachfragen nach weiteren Noten.
        if note_input == "x": 
            if counter > 0:
                break
            
            else:
                print("Bitte geben Sie mindestens eine Note ein.")

        # Prüft auf ungültige Usereingaben.
        else:
            try:
                note_float = float(note_input)

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
    notenschnitt = notenschnitt_berechnen()
    print(f"\nIhr Notenschnitt für das Fach {fach} ist {notenschnitt:.2f}.\n")
    notenliste[str(fach)] = float(notenschnitt)

def main():
    notenschnitte_auflisten()
    question_continue = "Möchten Sie eine weiteres Fach erfassen?\nBitte mit 'y' für Yes/Ja oder 'n' für No/Nein antworten: "
    abfrage = input(question_continue)

    while True:
        if abfrage != "y" and abfrage != "n":
            abfrage = input("Ungültige Eingabe. " + question_continue)
        
        elif abfrage == "y":
            notenschnitte_auflisten()
            abfrage = input(question_continue)
        
        elif abfrage == "n":
            break
    
    notensumme_gesamt = sum(notenliste.values())
    notenschnitt_gesamt = notensumme_gesamt / len(notenliste)

    print(f"\n------------------------------------------------")
    print(f"\nIhr Gesamtnotenschnitt beträgt {notenschnitt_gesamt:.2f}.\n")
    print(f"------------------------------------------------\n")
    print(f"Dies sind die Durchschnitte Ihrer Fächer:\n")
        
    for i in notenliste : 
        print(i, notenliste[i])

    print(f"\n------------------------------------------------")


if __name__ == "__main__":
    main()
