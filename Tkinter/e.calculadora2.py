import tkinter as tk
def sumar():
    try:
        n1=float(entrada1.get())
        n2=float(entrada2.get())
        result.set("error")
    except valueError:
        resultado.set("Error")
ventana=tk.Tk()
ventana.title("calculadora basica")
ventana.geometry("250x180")
resultado=tk.stringvar()
tk.laber(ventana,text="numero1:").pack(pady=5)
entreada1=tk.entry(ventana)
entreada1.pack()
tk.laber(ventana,text="numero2:").pack(pady=5)
entreada2=tk.entry(ventana)
entreada2.pack()
tk.Botton(ventana,text="sumar",command=sumar)
tk.laber(ventana,text="resultado:").pack
tk.leber(ventana,textvariable=resultado,fg="blue")
