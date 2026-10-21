# Operacje na SQLite
import sqlite3
from pathlib import Path
from termcolor import colored

def zapisz_do_bazy(df):
    if df is None or df.empty:
        print(colored("Najpierw wczytaj dane z pliku CSV", "red"))
        return

    folder = Path("database")
    folder.mkdir(exist_ok=True)

    sciezka = folder / "analizy.db"

    with sqlite3.connect(sciezka) as polaczenie:

        polaczenie.execute(
            """
            CREATE TABLE IF NOT EXISTS pomiary (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                miasto TEXT NOT NULL,
                temp_min REAL,
                temp_max REAL,
                wilgotnosc REAL,
                opady REAL,
                UNIQUE(data, miasto)
            )
            """
        )

        for _, wiersz in df.iterrows():
            polaczenie.execute(
                """
                INSERT OR IGNORE INTO pomiary
                (data, miasto, temp_min, temp_max, wilgotnosc, opady)
                VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    str(wiersz["data"]),
                    str(wiersz["miasto"]),
                    float(wiersz["temp_min"]),
                    float(wiersz["temp_max"]),
                    float(wiersz["wilgotnosc"]),
                    float(wiersz["opady"])
                )
            )
