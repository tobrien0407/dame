# main.py

import spielfeld
import zug

def spielerwechsel(aktueller_spieler):
    """Wechselt den aktuellen Spieler."""
    return 'X' if aktueller_spieler == 'O' else 'O'

def main():
    """Hauptspiel-Funktion."""
    print("Willkommen zum Dame-Spiel!")

    spielfeld.generiere_spielfeld()
    
    aktueller_spieler = 'X'  # Startspieler ist 'X'

    while True:
        print(f"Zug für Spieler {aktueller_spieler}:")
        start_pos = zug.startposition()
        ziel_pos = zug.zielposition()

        # Bewege den Stein und aktualisiere das Spielfeld
        spielfeld.bewege_stein(start_pos, ziel_pos, aktueller_spieler)

        # Überprüfe, ob der aktuelle Spieler noch gültige Züge hat
        if not spielfeld.spieler_hat_kuerzel(aktueller_spieler):
            print(f"Spieler {aktueller_spieler} hat keine Steine mehr. Spieler {spielerwechsel(aktueller_spieler)} gewinnt!")
            break
        
        # Wechsel den Spieler
        aktueller_spieler = spielerwechsel(aktueller_spieler)

if __name__ == "__main__":
    main()
