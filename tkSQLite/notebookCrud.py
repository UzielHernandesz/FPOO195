import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from Controlador import Controlador

objControlador = Controlador()

def ejecutaInsert():
    objControlador.insertUsuario(var1.get(), var2.get(), var3.get())
    
def busUsuario():
    usuarioBD= objControlador.buscarUsuario(varBus.get())
    if usuarioBD == []:
        messagebox.showwarning("Nada", "Id no existe en BD")
    else:
        resultado_text.config(state="normal")
        resultado_text.delete(1.0, tk.END) 
        resultado_text.insert(tk.END, usuarioBD)
        resultado_text.config(state="disabled")


def buscartodosusu():
    
    usuarios = objControlador.consultarTodosUsuarios()
    # Crear la tabla 
    ttk.Label(Consultarusuarios, text="ID").grid(row=0, column=0, padx=5, pady=5)
    ttk.Label(Consultarusuarios, text="Nombre").grid(row=0, column=1, padx=5, pady=5)
    ttk.Label(Consultarusuarios, text="Correo").grid(row=0, column=2, padx=5, pady=5)
    ttk.Label(Consultarusuarios, text="Contraseña").grid(row=0, column=3, padx=5, pady=5)
    for i, usuario in enumerate(usuarios, start=1):
        ttk.Label(Consultarusuarios, text=usuario[0]).grid(row=i, column=0, padx=5, pady=5)
        ttk.Label(Consultarusuarios, text=usuario[1]).grid(row=i, column=1, padx=5, pady=5)
        ttk.Label(Consultarusuarios, text=usuario[2]).grid(row=i, column=2, padx=5, pady=5)
        ttk.Label(Consultarusuarios, text=usuario[3]).grid(row=i, column=3, padx=5, pady=5)
        
        
        #print(usuarioBD)

ventana = tk.Tk()
ventana.title("CRUD de Usuarios")
ventana.geometry("500x300")

panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand="yes")

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)

panel.add(pestana1, text="Crear usuario")
panel.add(pestana2, text="Buscar usuario")
panel.add(pestana3, text="Consultar usuario")
panel.add(pestana4, text="Editar usuario")
panel.add(pestana5, text="Eliminar usuario")

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

# Pestaña 2: Buscar Usuario
tk.Label(pestana2, text="Buscar Usuario", fg="blue", font=("Modern", 18)).pack()

# Creación del campo de entrada para el ID con su respectiva etiqueta.
varBus = tk.StringVar()
tk.Label(pestana2, text="Id: ").pack()
tk.Entry(pestana2, textvariable=varBus).pack()

# Botón para buscar el usuario. Llama a la función buscarUsuario cuando se hace clic.
tk.Button(pestana2, text="Buscar Usuario", command=busUsuario).pack()

# Widget de texto para mostrar el resultado de la búsqueda.
resultado_text = tk.Text(pestana2, height=5, width=52)
resultado_text.pack()


# Pestaña 3: Consultar todos los usuarios
tk.Label(pestana3, text="Consulta Todos Usuarios", fg="blue", font=("Mono", 18)).pack()

# Frame para mostrar la información de los usuarios consultados
Consultarusuarios = ttk.Frame(pestana3)
Consultarusuarios.pack(padx=10, pady=10)

# Botón para consultar todos los usuarios
tk.Button(pestana3, text="Consulta Todos Usuarios", command=buscartodosusu).pack()
# # #pestaña 3
# tk.Label(pestana3, text="Consulta Todos Usuarios", fg="blue", font=("Mono", 18)).pack()
# tk.Button(pestana3, text="Consulta Todos Usuarios", command=buscartodosusu).pack()


# # Inicia el bucle principal de la interfaz gráfica. Mantiene abierta la ventana hasta que el usuario decida cerrarla.
ventana.mainloop()

# tk.Label(pestana2, text="Buscar usuario", fg="red", font=("Mono", 18)).pack()

# varBus = tk.StringVar()
# tk.Label(pestana2, text="Id: ").pack()
# tk.Entry(pestana2, textvariable=varBus).pack()

# tk.Button(pestana2, text="Buscar usuario", command=busUsuario).pack()

# tk.Label(pestana2, text="Registrado", fg="blue", font=("Mono", 16)).pack()
# tk.Text(pestana2, height=5, width=52).pack()


# ventana.mainloop()
