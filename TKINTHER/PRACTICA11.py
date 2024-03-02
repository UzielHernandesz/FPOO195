from tkinter import Tk, Frame
#son clases las de arriba
#una libreria esta compuesta de muchas clases
#1. Creamos la ventana

Ventana = Tk() # Instancia para la clase TK, uso de poo, creando un obj ventana
Ventana.title("Ejemplo con 3 Frames")
Ventana.geometry("600x400")



#2. colocar las secciones de la ventana
seccion1 = Frame(Ventana, bg= "red")
seccion1.pack(expand=True, fill='both')

seccion2 = Frame(Ventana, bg= "green")
seccion2.pack(expand=True, fill= 'both')

seccion3 = Frame(Ventana, bg= "Black")
seccion3.pack(expand=True, fill='both')






#Para que se ejecute, metodo
Ventana.mainloop()

