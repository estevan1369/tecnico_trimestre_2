import tkinter as tk 

root = tk.Tk()
root.title("calculadora")
root.geometry("400x450")

decoracion = tk.libel(root,text=decoracion:)
decoracion.pack (pady=10)

entry_decoracion = tk. Entry(root)
entry_decoracion.pack (pady=10)

def calcular_total():
      try:
        decoracion = float(entry_decoracion.get() or 0)
        Musica = float(entry_musica.get() or 0)
        comida = float(entry_comida.get() or 0)
        transporte = float(entry_transporte.get() or 0)
        total = decoracion + Musica + comida + transporte

