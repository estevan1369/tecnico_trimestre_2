import tkinter 
ventana = tkinter.Tk(screenName=None, baseName=None, className='Tk', useTk=1)
ventana.geometry("400x300")
boton1 = tkinter. Button(ventana,text="boton1", width=10,height=5)
boton2= tkinter. Button(ventana,text="boton2", width=10,height=5)
boton3=tkinter. Button(ventana,text="boton3", width=10,height=5)

boton1.grid(row = 0, column = 0)
boton2.grid(row = 1, column = 0)
boton3.grid(row = 2, column = 0)

ventana.maintoop()