import csv
import os
import tkinter as tk
from tkinter import messagebox

def carica_reazioni(file_path):
    reazioni = {}
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                reazioni[row[0]] = row[1]
    except FileNotFoundError:
        print(f"File {file_path} non trovato, sarà creato un nuovo file.")
    return reazioni

def salva_reazioni(file_path, reazioni):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        for reagenti, prodotto in reazioni.items():
            writer.writerow([reagenti, prodotto])

def ricerca_reazione():
    elemento1 = entry_elemento1.get()
    elemento2 = entry_elemento2.get()

    if not elemento1 or not elemento2:
        messagebox.showwarning("Input mancante", "Inserire entrambi gli elementi.")
        return

    elementi_reazione = elemento1 + "+" + elemento2

    if elementi_reazione in reazioni:
        risultato = reazioni[elementi_reazione]
        label_risultato.config(text=f"{elementi_reazione} ---> {risultato}")
        label_nuovo_prodotto.grid_remove()  # Nascondi l'etichetta "Nuovo Prodotto"
        entry_nuovo_prodotto.grid_remove()  # Nascondi il campo del nuovo prodotto
        button_salva.grid_remove()  # Nascondi il pulsante per salvare
    else:
        label_risultato.config(text="Reazione non trovata")
        label_nuovo_prodotto.grid(row=4, column=0, padx=10, pady=10)  # Mostra l'etichetta "Nuovo Prodotto"
        entry_nuovo_prodotto.grid(row=4, column=1, padx=10, pady=10)  # Mostra il campo del nuovo prodotto
        button_salva.grid(row=5, column=0, columnspan=2, pady=10)  # Mostra il pulsante per salvare

def salva_nuova_reazione():
    elemento1 = entry_elemento1.get()
    elemento2 = entry_elemento2.get()
    nuovo_prodotto = entry_nuovo_prodotto.get()

    if not nuovo_prodotto:
        messagebox.showwarning("Input mancante", "Inserire il prodotto della reazione.")
        return

    elementi_reazione = elemento1 + "+" + elemento2
    reazioni[elementi_reazione] = nuovo_prodotto
    salva_reazioni(file_path, reazioni)
    messagebox.showinfo("Reazione aggiunta", f"Nuova reazione aggiunta: {elementi_reazione} ---> {nuovo_prodotto}")
    entry_nuovo_prodotto.delete(0, tk.END)  # Pulisci il campo del nuovo prodotto
    label_risultato.config(text="")
    label_nuovo_prodotto.grid_remove()  # Nascondi l'etichetta "Nuovo Prodotto"
    entry_nuovo_prodotto.grid_remove()  # Nascondi il campo del nuovo prodotto
    button_salva.grid_remove()  # Nascondi il pulsante per salvare

# Ottieni il percorso della directory dello script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Path del file CSV nella stessa directory dello script
file_path = os.path.join(script_dir, "database_reazioni.csv")

# Caricamento delle reazioni dal file CSV
reazioni = carica_reazioni(file_path)

# Creazione della finestra principale
root = tk.Tk()
root.title("Database Reazioni Chimiche")

# Creazione dei widget
label_elemento1 = tk.Label(root, text="Elemento 1:")
label_elemento1.grid(row=0, column=0, padx=10, pady=10)

entry_elemento1 = tk.Entry(root)
entry_elemento1.grid(row=0, column=1, padx=10, pady=10)

label_elemento2 = tk.Label(root, text="Elemento 2:")
label_elemento2.grid(row=1, column=0, padx=10, pady=10)

entry_elemento2 = tk.Entry(root)
entry_elemento2.grid(row=1, column=1, padx=10, pady=10)

button_ricerca = tk.Button(root, text="Cerca Reazione", command=ricerca_reazione)
button_ricerca.grid(row=2, column=0, columnspan=2, pady=10)

label_risultato = tk.Label(root, text="")
label_risultato.grid(row=3, column=0, columnspan=2, pady=10)

label_nuovo_prodotto = tk.Label(root, text="Nuovo Prodotto:")
label_nuovo_prodotto.grid(row=4, column=0, padx=10, pady=10)
label_nuovo_prodotto.grid_remove()  # Nascondi inizialmente l'etichetta "Nuovo Prodotto"

entry_nuovo_prodotto = tk.Entry(root)
entry_nuovo_prodotto.grid(row=4, column=1, padx=10, pady=10)
entry_nuovo_prodotto.grid_remove()  # Nascondi inizialmente il campo del nuovo prodotto

button_salva = tk.Button(root, text="Salva Reazione", command=salva_nuova_reazione)
button_salva.grid(row=5, column=0, columnspan=2, pady=10)
button_salva.grid_remove()  # Nascondi inizialmente il pulsante di salvataggio

# Avvio del loop principale
root.mainloop()












#Fine del codice
# ---------------------------------------------
# Copyright (c) 2024 Mario Pisano
#
# Questo programma è distribuito sotto la licenza EUPL, Versione 1.2 o – non appena 
# saranno approvate dalla Commissione Europea – versioni successive della EUPL 
# (la "Licenza");
# Puoi usare, modificare e/o ridistribuire il programma sotto i termini della 
# Licenza. 
# 
# Puoi trovare una copia della Licenza all'indirizzo:
# https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12
