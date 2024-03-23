import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Controlador import Controlador

objControlador = Controlador()

def ejecutaInsert():
    objControlador.insertUsuario(var1.get(), var2.get(), var3.get())

ventana = tk.Tk()
ventana.title("CRUD de Usuarios")
ventana.geometry("500x300")

panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand="yes")

pestana1 = ttk.Frame(panel)
panel.add(pestana1, text="Crear usuario")

tk.Label(pestana1, text="Registro de Usuarios", fg="blue", font=("Modern", 18)).pack()

var1 = tk.StringVar()
tk.Label(pestana1, text="Nombre: ").pack()
tk.Entry(pestana1, textvariable=var1).pack()

var2 = tk.StringVar()
tk.Label(pestana1, text="Correo: ").pack()
tk.Entry(pestana1, textvariable=var2).pack()

var3 = tk.StringVar()
tk.Label(pestana1, text="Contraseña: ").pack()
tk.Entry(pestana1, textvariable=var3).pack()

tk.Button(pestana1, text="Guardar usuario", command=ejecutaInsert).pack()

ventana.mainloop()
