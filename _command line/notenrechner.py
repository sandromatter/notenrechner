notenliste = {}

def fach_abfrage():
    fach_eingabe = str(input("Von welchem Fach möchten Sie die Noten berechnen? "))
    fach_eingabe = fach_eingabe.capitalize()

    return fach_eingabe

def notenschnitt_berechnen():
    noten = []
    counter = 0
    question_data = "Geben Sie Ihre Note (1-6) ein oder x um abzubrechen: "

    while True:
        note_input = input(question_data)

        if note_input == "x":
            if counter > 0:
                break
            
            else:
                print("Bitte geben Sie mindestens eine Note ein.")

        else:
            try:
                note_float = float(note_input)

                if note_float >= 1.0 and note_float <= 6.0:
                    noten.append(note_float)
                    counter += 1

            except ValueError:
                print("Ungültige Eingabe")
        

    notensumme = sum(noten)
    notenschnitt = notensumme / counter

    return notenschnitt

def fach_notenschnitt_dict():
    fach = fach_abfrage()
    notenschnitt = notenschnitt_berechnen()
    print(f"\nIhr Notenschnitt für das Fach {fach} ist {notenschnitt}.\n")
    notenliste[str(fach)] = float(notenschnitt)

def main():
    fach_notenschnitt_dict()
    question_continue = "Möchten Sie eine weiteres Fach erfassen?\nBitte mit 'y' oder 'n' antworten: "
    abfrage = input(question_continue)

    while True:
        if abfrage != "y" and abfrage != "n":
            abfrage = input("Ungültige Eingabe. " + question_continue)
        
        elif abfrage == "y":
            fach_notenschnitt_dict()
            abfrage = input(question_continue)
        
        elif abfrage == "n":
            break
    
    notensumme_gesamt = sum(notenliste.values())
    notenschnitt_gesamt = notensumme_gesamt / len(notenliste)

    print(f"Ihr Gesamtnotenschnitt beträgt {notenschnitt_gesamt}.")
    print(f"Dies sind die Durchschnitte Ihrer Fächer:")
        
    for i in notenliste : 
        print(i, notenliste[i])


if __name__ == "__main__":
    main()
