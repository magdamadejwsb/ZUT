# Uruchamianie aplikacji
from interfejs import uruchum_menu

def main():
    uruchum_menu()

# warunek uruchamiania programu - określa czy dany plik został uruchomiany bezpośrednio, czy został zaimportowany jako moduł z innego pliku
# __name__ - zmiena automatycznie ustawiana przez Pythona dla każdego modułu
# "__main__" - wartość oznaczająca moduł uruchamiany jako główny program

if __name__ == "__main__":
    main()    