# spielfeld.py

# Initialisiere das Spielfeld
spielfeld = [
    ['#', 'X', '#', 'X', '#', 'X', '#', 'X'],
    ['X', '#', 'X', '#', 'X', '#', 'X', '#'],
    ['#', 'X', '#', 'X', '#', 'X', '#', 'X'],
    [' ', '#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', ' '],
    ['O', '#', 'O', '#', 'O', '#', 'O', '#'],
    ['#', 'O', '#', 'O', '#', 'O', '#', 'O'],
    ['O', '#', 'O', '#', 'O', '#', 'O', '#'],
]

def generiere_spielfeld():
    """Gibt das Spielfeld im gewünschten Format aus."""
    print("    A   B   C   D   E   F   G   H")  # Spaltenbezeichnung
    print("  +---+---+---+---+---+---+---+---+")  # Obere Trennlinie

    for i, row in enumerate(spielfeld):
        print(f"{i+1} | " + " | ".join(row) + " |")  # Zeilenbezeichnung und Spielfeldinhalte
        print("  +---+---+---+---+---+---+---+---+")  # Trennlinie nach jeder Zeile
def ist_gueltioger_zug(start, ziel, spieler):
    """Überprüft, ob der Zug gültig ist (Bewegung und Schlagen)."""
    reihe_start, spalte_start = start
    reihe_ziel, spalte_ziel = ziel
    stein = spielfeld[reihe_start][spalte_start]
    ziel_stein = spielfeld[reihe_ziel][spalte_ziel]

    # Überprüfe, ob das Ziel leer ist
    if ziel_stein != ' ':
        return False
    
    # Überprüfe, ob der Zug ein Schlagen ist
    if abs(reihe_start - reihe_ziel) == 2 and abs(spalte_start - spalte_ziel) == 2:
        reihe_mittel, spalte_mittel = (reihe_start + reihe_ziel) // 2, (spalte_start + spalte_ziel) // 2
        mittel_stein = spielfeld[reihe_mittel][spalte_mittel]
        if mittel_stein in ['X', 'O'] and mittel_stein != spieler:
            return True
    # Überprüfe, ob der Zug normal gültig ist
    elif abs(reihe_start - reihe_ziel) == 1 and abs(spalte_start - spalte_ziel) == 1:
        if spielfeld[reihe_ziel][spalte_ziel] == ' ':
            return True
    # Überprüfe Dame-Zug
    elif stein.upper() == 'D':
        if abs(reihe_start - reihe_ziel) == abs(spalte_start - spalte_ziel):
            if all(spielfeld[reihe][spalte] == ' ' for reihe in range(min(reihe_start, reihe_ziel)+1, max(reihe_start, reihe_ziel)) 
                                                    for spalte in range(min(spalte_start, spalte_ziel)+1, max(spalte_start, spalte_ziel))):
                return True
    
    return False

def bewege_stein(start, ziel, spieler):
    """Bewegt einen Stein von der Startposition zur Zielposition auf dem Spielfeld."""
    reihe_start, spalte_start = start
    reihe_ziel, spalte_ziel = ziel

    if not ist_gueltioger_zug(start, ziel, spieler):
        print("Der Zug ist ungültig.")
        return

    if abs(reihe_start - reihe_ziel) == 2 and abs(spalte_start - spalte_ziel) == 2:
        reihe_mittel, spalte_mittel = (reihe_start + reihe_ziel) // 2, (spalte_start + spalte_ziel) // 2
        spielfeld[reihe_mittel][spalte_mittel] = ' '

    spielfeld[reihe_start][spalte_start] = ' '
    spielfeld[reihe_ziel][spalte_ziel] = spieler
    
    # Umwandeln in eine Dame
    if reihe_ziel == 0 and spieler == 'X':
        spielfeld[reihe_ziel][spalte_ziel] = 'D'
    elif reihe_ziel == 7 and spieler == 'O':
        spielfeld[reihe_ziel][spalte_ziel] = 'd'

    generiere_spielfeld()

def spieler_hat_kuerzel(spieler):
    """Überprüft, ob ein Spieler noch Steine auf dem Spielfeld hat."""
    for row in spielfeld:
        if spieler in row:
            return True
    return False
