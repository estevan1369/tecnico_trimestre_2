import tkinter 
ventana=tkinter.Tk()
ventana.geometry("400x300")
cajaTexto= tkinter.Entry(ventana)
cajaTexto.pack()
def textoDeLacaja():
    text20=cajaTexto.get()
    print(text20)


boton1 =tkinter.Button(ventana, text="click",command= textoDeLacaja)
boton1.pack()
ventana.mainloop()