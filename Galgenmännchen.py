from random import choice

def spiel_start():
    wort : str = choice(["Apfel", "Banane", "Haus", "Auto", "Schule", "Stuhl", "Tisch", "Fenster", "Telefon", "Buch", "Katze", "Hund", "Baum", "Blume", "Fluss", "Wald", "Berg", "See", "Mond", "Sonne", "Tasse", "Löffel", "Gabel", "Messer", "Stadt", "Land", "Welt", "Universität", "Park", "Straße", "Wolke", "Regen", "Schnee", "Wind", "Feuer", "Erde", "Luft", "Wasser", "Sand", "Stein", "Gold", "Silber", "Kupfer", "Eisen", "Stahl", "Ziegel", "Zement", "Glas", "Plastik", "Papier", "Stoff", "Holz", "Metall", "Geld", "Zeit", "Tag", "Nacht", "Woche", "Monat", "Jahr", "Minute", "Stunde", "Sekunde", "Frage", "Antwort", "Problem", "Lösung", "Idee", "Plan", "Projekt", "Aufgabe", "Ziel", "Traum", "Wunsch", "Gedanke", "Gefühl", "Emotion", "Liebe", "Hass", "Freude", "Trauer", "Angst", "Mut", "Hoffnung", "Glück", "Pech", "Zufall", "Schicksal", "Kunst", "Musik", "Malerei", "Literatur", "Film", "Theater", "Sport", "Spiel", "Reise", "Abenteuer", "Erlebnis", "Erfahrung", "Entdeckung"])
    spielername : str = input("Wie heißt du? ")
    print(f"Viel Spaß mit Galgenmännchen {spielername} :)")

    geraten : str = ""
    versuche : int = 5


    while versuche > 0:
        leere_felder : int = 0

        print("Wort: ", end="")
        for char in wort:
            if char in geraten:
                print(char, end="")
            else:
                print("_", end="")
                leere_felder += 1

        print() 

        if leere_felder == 0:
            print("Du hast gewonnen :D")
            break


        antwort : str = input("Gib einen Buchstaben ein: ")

        if antwort in geraten:
            print(f"Du hast bereits {antwort} benutzt. Bitte benutze einen anderen Buchstaben.")
            continue

        geraten += antwort

        if antwort not in wort:
            versuche -= 1
            print(f"Das war leider falsch (Du hast noch {versuche} Versuche)")   

            if versuche == 0:
                print("Du hast leider verloren :(")
                break


if __name__ == "__main__":
    spiel_start()











