# zug.py

def startposition():
    """Fragt die Startposition des Benutzers ab und wandelt sie in Indizes um."""
    while True:
        position = input("Gib die Startposition ein (z.B. A3): ").upper()
        index = eingabe_konvertieren_index(position)
        if index is not None:
            reihe_index, spalte_index = index
            if 0 <= reihe_index < 8 and 0 <= spalte_index < 8:
                return reihe_index, spalte_index
            else:
                print("Die eingegebene Position liegt außerhalb des gültigen Bereichs. Versuche es erneut.")
        else:
            print("Ungültige Eingabe. Stelle sicher, dass die Position im Format 'A1' bis 'H8' vorliegt.")

def zielposition():
    """Fragt die Zielposition des Benutzers ab und wandelt sie in Indizes um."""
    while True:
        position = input("Gib die Zielposition deines Steins ein (z.B. A3): ").upper()
        index = eingabe_konvertieren_index(position)
        if index is not None:
            reihe_index, spalte_index = index
            if 0 <= reihe_index < 8 and 0 <= spalte_index < 8:
                return reihe_index, spalte_index
            else:
                print("Die eingegebene Position liegt außerhalb des gültigen Bereichs. Versuche es erneut.")
        else:
            print("Ungültige Eingabe. Stelle sicher, dass die Position im Format 'A1' bis 'H8' vorliegt.")

def eingabe_konvertieren_index(position):
    """Wandelt eine Benutzereingabe wie 'A3' in Spielfeld-Indices um."""
    spalten = 'ABCDEFGH'
    if len(position) == 2 and position[0] in spalten and position[1].isdigit():
        spalte_index = spalten.index(position[0])
        reihe_index = int(position[1]) - 1
        return reihe_index, spalte_index
    else:
        print(f"Ungültige Position eingegeben: {position}")
        return None
