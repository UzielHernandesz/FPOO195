from tkinter import Usuario, Frame, Button, messagebox
from tkinter import *
from tkinter import ttk


ventana = Tk()
ventana.title("login")
ventana.geometry("700x600")

seccion = Frame(ventana, bg="gray")
seccion.pack(expand=True, fill="both")

titulo = Label(seccion, text="Login.", font=("Abadi", 18))
titulo.place(x=230, y=20)

caja1 = ttk.Entry(seccion)
caja1.place(x=250, y=80, width=100, height=40)

seccion2 = Frame(ventana, bg="green")
seccion2.pack(expand=True, fill="both")

input2 = ttk.Entry(seccion2, show="*")
input2.place(x=270, y=50, width=100, height=40)




ventana.mainloop()