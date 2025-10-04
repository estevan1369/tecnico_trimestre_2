import tkinter
ventana=tkinter.TK()
ventana.geometry("400x300")
cajaTexto= tkinter.Entry(ventana)
cajaTexto.pack()
def textoDeLacaja():
    text20=cajaTexto.get()
    print(text20)


boton1 =tkinter.Button(ventana, text="click",command= textoDelaCaja)
boton1.pack()
ventana.mainloop()