# Wczytywanie danych z pliku CSV
from pathlib import Path
from termcolor import colored
import pandas as pd


def wczytaj_dane():
    folder = Path("data")
    # metoda glob() msłuży do wyszukiwania plików pasujących do określonego wzorca
    pliki = sorted(folder.glob("*.csv"))

    if not pliki:
        print(colored(f"Brak plików w {folder}", "red"))
        return None

    print(colored("\nDOSTĘPNE PLIKI CSV", "blue"))

    if len(pliki) <= 10:
        for numer, plik in enumerate(pliki, start=1):
                print(f"{numer}. {plik.name}")
    else:            
        for numer, plik in enumerate(pliki[:2], start=1):
            print(f"{numer}. {plik.name}")
    
        print("...")

        print(f"{len(pliki)}. {pliki[-1].name}")

    print("0. Powrót do menu głównego.")

    # pętla while obsługująca wybór pliku do analizy
    while True:
        wybor = input("\nWybierz numer pliku: ")

        if wybor == "0":
            return None

        if not wybor.isdigit():
            print(colored("Podaj poprawny numer", "red"))
            continue

        numer = int(wybor)

        if numer > len(pliki):
            print(colored("Nie ma pliku o takim numerze", "red"))
            continue

        wybrany_plik = pliki[numer - 1]

        try:
            df = pd.read_csv(wybrany_plik)
        except pd.errors.ParserError as blad:
            print(colored(f"Błąd wczytania pliku: {blad}", "red"))    
            return None

        print(colored(f"\nWczytano plik: {wybrany_plik.name}", "green"))
        print(f"Liczba wierszy: {len(df)}")

        return df


def wyswietl_dane(df):
    if df is None:
        print(colored("\nNajpierw wczytaj plik CSV", "red"))
        return

    print("\n***** PODGLĄD DANYCH *****")

    print("Pierwsze 10 wierszy")
    print(df.head(10).to_string(index=False))

    print("\nInformacje o zbiorze:")
    print(f"Liczba rekordów: {df.shape[0]}")
    print(f"Liczba kolumn: {df.shape[1]}")
    print(f"Koluny: {', '.join(df.columns)}")