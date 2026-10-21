# Generowanie wykresów
from pathlib import Path
import os

import matplotlib.pyplot as plt
import pandas as pd
from termcolor import colored

def generuj_wykres(df):
    if df is None or df.empty:
        print(colored("Najpierw wczytaj dane z pliku CSV", "red"))
        return

    dane = df.copy()
    dane["data"] = pd.to_datetime(dane["data"])

    fig, ax = plt.subplots()

    for miasto, pomiary in dane.groupby("miasto"):
        pomiary = pomiary.sort_values("data")

        ax.plot(
            pomiary["data"],
            pomiary["temp_max"],
            label=miasto
        )

    ax.set_title("Temperatura maksymalna w czasie")
    ax.set_xlabel("Data")
    ax.set_ylabel("temperatura [℃]")
    ax.legend()
    ax.grid(True, color="#ddd", linestyle="-.")

    fig.autofmt_xdate()

    # zapis do pliku
    folder = Path("results")
    folder.mkdir(exist_ok=True)

    nazwa = f"wykres_{dane["data"].min():%Y_%m}.png"
    sciezka = folder / nazwa

    fig.savefig(sciezka)

    if os.path.exists(sciezka):
        print(colored(f"Zapisano wykres: {sciezka}", "green"))
    else:
        print(colored("Plik nie został znaleziony", "red") )   

    plt.show()
    plt.close(fig)