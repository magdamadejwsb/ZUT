"""Interfejs konsolowy aplikacji"""
from termcolor import colored
from dane import wczytaj_dane, wyswietl_dane
from analiza import podstawowe_statystyki
from wykresy import generuj_wykres
from baza import zapisz_do_bazy


def wyswietl_menu():
    print("\n\nRESEARCH DATA ANALYZER")
    print("1. Wczytaj dane z pliku csv")
    print("2. Wyświetl dane")
    print("3. Analizuj dane")
    print("4. Generuj i zapisz wykres")
    print("5. Zapisz dane do bazy")
    print("0. Wyjście z programu")
    print(colored("-" * 40, "blue"))

def uruchum_menu():
    dane = None

    while True:
        wyswietl_menu()    
        wybor = input("Wybierz opcję: ").strip()

        if wybor == "0":
            print(colored("Zakończono dziłanie programu", "green"))
            break

        elif wybor == "1":
            print("wybrano opcje 1")
            nowe_dane = wczytaj_dane()

            if nowe_dane is not None:
                dane = nowe_dane

        elif wybor == "2":
            print("wybrano opcje 2") 
            wyswietl_dane(dane)

        elif wybor == "3":
            print("wybrano opcje 3")
            podstawowe_statystyki(dane)

        elif wybor == "4":
            print("wybrano opcje 4")
            generuj_wykres(dane)

        elif wybor == "5":
            print("wybrano opcje 5")  
            zapisz_do_bazy(dane)

        else:
            print(colored("Nieprawidłowa opcja. Spróbuj ponownie", "red"))