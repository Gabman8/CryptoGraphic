import tkinter as tk
from tkinter import ttk
import buildGraphic  # tu archivo donde está load_graphic()

def on_generate_click():
    symbol = symbol_entry.get()
    days = int(days_entry.get())
    buildGraphic.load_graphic(symbol, days)

# Crear ventana
root = tk.Tk()
root.title("Crypto Trend Analyzer")
root.geometry("350x200")

# Título
title = ttk.Label(root, text="Analizador de tendencias de Criptomonedas", font=("Arial", 12, "bold"))
title.pack(pady=10)

# Entrada de símbolo
symbol_label = ttk.Label(root, text="Criptomoneda (ej: Bitcoin, Ethereum):")
symbol_label.pack()
symbol_entry = ttk.Entry(root)
symbol_entry.pack()

# Entrada de días
days_label = ttk.Label(root, text="Días de análisis (ej: 30):")
days_label.pack()
days_entry = ttk.Entry(root)
days_entry.pack()

# Botón
generate_button = ttk.Button(root, text="Generar Gráfico", command=on_generate_click)
generate_button.pack(pady=15)

root.mainloop()
