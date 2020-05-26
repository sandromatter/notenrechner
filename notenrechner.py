notenliste = {}


# Abfrage des Faches.
def fach_abfragen():
    call_fach = "\nVon welchem Fach möchten Sie die Noten berechnen? "
    fach_eingabe = str(input(call_fach))
    fach_eingabe = fach_eingabe.capitalize()

    # Prüft ob das Fach bereits erfasst wurde.
    if fach_eingabe in notenliste:
        print(f"\nAchtung! Sie haben dieses Fach bereits erfasst.")
        call_type_again = f"Geben Sie '{fach_eingabe}' nochmals ein, um den Notenschnitt für das bestehende Fach zu löschen und neu zu erfassen oder 'x' um abzubrechen: "
        abfrage_fach = str(input(call_type_again))
            
        while True:
            if abfrage_fach != "x" and abfrage_fach != f"{fach_eingabe}":
                abfrage_fach = input("Ungültige Eingabe.\n" + call_type_again)

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
    question_data = "Geben Sie Ihre Note (1-6) ein oder 'x' um abzubrechen: "

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

    # Fügt neues Fach und Notenschnitt zur Notenliste.
    if fach != None:
        notenschnitt = notenschnitt_berechnen()
        print(f"\nIhr Notenschnitt für das Fach {fach} ist {notenschnitt:.2f}.\n")
        notenliste[str(fach)] = float(notenschnitt)


# Main Programm, fragt beim User nach weiterer Eingabe.
def main():
    notenschnitte_auflisten()
    question_continue = "Möchten Sie eine weiteres Fach erfassen?\nBitte mit 'y' für Yes/Ja oder 'n' für No/Nein antworten: "
    abfrage_weitere = input(question_continue)

    # Checkt ob weitere Eingabe gewünscht ist bis User mit 'Nein' abbricht.
    while True:
        if abfrage_weitere != "y" and abfrage_weitere != "n":
            abfrage_weitere = input("Ungültige Eingabe.\n" + question_continue)
        
        elif abfrage_weitere == "y":
            notenschnitte_auflisten()
            abfrage_weitere = input(question_continue)
        
        elif abfrage_weitere == "n":
            break
    
    notensumme_gesamt = sum(notenliste.values())
    notenschnitt_gesamt = notensumme_gesamt / len(notenliste)

    print(f"\n------------------------------------------------")
    print(f"\nIhr Gesamtnotenschnitt beträgt {notenschnitt_gesamt:.2f}.\n")
    print(f"------------------------------------------------\n")
    print(f"Dies sind die Durchschnitte Ihrer Fächer:\n")
        
    for i in notenliste : 
        print(f"{i}:\t\t\t{notenliste[i]:.2f}")

    print(f"\n------------------------------------------------")


if __name__ == "__main__":
    main()
