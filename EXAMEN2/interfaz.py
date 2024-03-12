from tkinter import Tk,Frame, Button,Label,messagebox, Entry
import tkinter as tk


class Login:
    

        Ventana = Tk()
        Ventana.title("Login Persona")
        Ventana.geometry("800x600")

        seccion1 = Frame(Ventana)
        seccion1.pack(expand=True, fill='both')

        Label(seccion1, text="Examen2P", bg="black", fg="white", font=("Mono", 18)).pack()

        var1 = tk.StringVar()
        Label(seccion1, text="Nombre:", font=("Helvetica", 14)).pack()
        Entry(seccion1, takefocus=True, textvariable=var1).pack()

        var2 = tk.StringVar()
        Label(seccion1, text="Apellido Paterno:", font=("Helvetica", 14)).pack()
        Entry(seccion1, takefocus=True, textvariable=var1).pack()
        
        var3 = tk.StringVar()
        Label(seccion1, text="Apellido Materno", font=("Helvetica", 14)).pack()
        Entry(seccion1, takefocus=True, textvariable=var1).pack()
        
        var4 = tk.StringVar()
        Label(seccion1, text="Año Nacimiento:", font=("Helvetica", 14)).pack()
        Entry(seccion1, takefocus=True, textvariable=var1).pack()
        
        var5 = tk.StringVar()
        Label(seccion1, text="Carrera:", font=("Helvetica", 14)).pack()
        Entry(seccion1, takefocus=True, textvariable=var1).pack()
        
        
        messagebox.showinfo('Tu matricula es: ', ' No se pudo generar ')
        Ventana.mainloop()
