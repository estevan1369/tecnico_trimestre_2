import tkinter
ventana = tkinter.Tk()
ventana.geometry("400x300")
def saludo1():
    print("Hola")

boton1 = tkinter.Button(ventana, text ="Presiona", command = saludo1)
boton1.pack()
ventana.mainloop()