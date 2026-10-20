import random
import tkinter as tk
from pathlib import Path
from tkinter import ttk, filedialog, messagebox

# OKNO APLIKACJI

okno = tk.Tk()
okno.title("Exam Generator")
okno.geometry("600x360")
okno.resizable(False, False)

plik_pytan = tk.StringVar()
folder_wynikowy = tk.StringVar()

ramka = ttk.Frame(okno, padding=20)
ramka.pack(fill="both", expand=True)

ttk.Label(
    ramka,
    text="GENERATOR ZESTAWÓW EGZAMINACYJNYCH",
    font=("Arial", 14, "bold")
).grid(row=0, column=0, columnspan=3, pady=20)

ttk.Label(
    ramka, text="Baza pytań:"
).grid(row=1, column=0, sticky="w")

ttk.Entry(
    ramka, textvariable=plik_pytan, width=40
).grid(row=1, column=1, padx=10, pady=8)

ttk.Button(
    ramka, text="Wybierz", command=""
).grid(row=1, column=2)

ttk.Label(
    ramka, text="Liczba pytań:"
).grid(row=2, column=0, sticky="w")

pole_liczba_pytan = ttk.Entry(ramka, width=10)
pole_liczba_pytan.insert(0, "5")
pole_liczba_pytan.grid(row=2, column=1, sticky="w", padx=10)

ttk.Label(
    ramka, text="Liczba zestawów:"
).grid(row=3, column=0, sticky="w")

pole_liczba_zestawow = ttk.Entry(ramka, width=10)
pole_liczba_zestawow.insert(0, "3")
pole_liczba_zestawow.grid(row=3, column=1, sticky="w", padx=10)

ttk.Label(
    ramka, text="Folder wynikowy:"
).grid(row=4, column=0, sticky="w")

ttk.Entry(
    ramka, textvariable=folder_wynikowy, width=40
).grid(row=4, column=1, padx=10, pady=8)

ttk.Button(
    ramka, text="Wybierz", command=""
).grid(row=4, column=2)

ttk.Button(
    ramka,
    text="GENERUJ ZESTAWY",
    command=""
).grid(row=5, column=0, columnspan=3, pady=25)

status = ttk.Label(
    ramka, text="Oczekiwanie na dane..."
)
status.grid(row=6, column=0, columnspan=3)

okno.mainloop()
