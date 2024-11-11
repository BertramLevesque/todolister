#!/usr/bin/env python3

einträge = [
    {"name": "eins", "pos": "1", "fortschritt": "1", "bemerkung": "None"},
    {"name": "vier", "pos": "4", "fortschritt": "0", "bemerkung": "None"},
    {"name": "drei", "pos": "3", "fortschritt": "0", "bemerkung": "None"},
    {"name": "zwei", "pos": "2", "fortschritt": "0", "bemerkung": "None"}
]

def eintrag_hinzufügen(einträge):
    print("Platzhalter: hinzufügen")

def eintrag_anzeigen(einträge):
    if not einträge:
        print("Die ToDo-Liste ist leer.")
        return

    for eintrag in einträge:
        print("Name: ", eintrag["name"])
        print("Priorität: ", eintrag["pos"])
        print("Fortschritt: ", eintrag["fortschritt"])
        print("Bemerkung: ", eintrag["bemerkung"])

def eintrag_suchen(einträge):
    print("Platzhalter: suchen")

def eintrag_speichern(einträge):
    print("Platzhalter: speichern")


def main():

    while True:
        print("\n\n1. zur ToDo-Liste hinzufügen")
        print("2. ToDo-Liste anzeigen")
        print("3. Eintrag suchen")
        print("4. speichern und beenden")
        auswahl = input("\nAuswahl: ")
        if auswahl == "1":
            eintrag_hinzufügen(einträge)
        elif auswahl == "2":
            eintrag_anzeigen(einträge)
        elif auswahl == "3":
            eintrag_suchen(einträge)
        elif auswahl == "4":
            print("Programm beendet.")
            break
        else:
            print("Bitte im Bereich von 1 und 4 wählen.")


main()
