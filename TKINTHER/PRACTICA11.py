from tkinter import Tk, Frame, Button, messagebox

#metodos para mensaje al usar el boton

def mostrarMesaje():
    print(messagebox.showinfo('showinfo','Information'))
    print(messagebox.showerror('showerror','Error'))
    print(messagebox.showwarning('showwarning','Warning'))
    
    #mensajes para hacer preguntas, siempre asignar un mensaje y un titulo, en todos los de pregunta
    print(messagebox.askokcancel(message="¿Desea continuar?", title="Soy el titulo"))



# nuevo metodo 

def addbtn():
    botonVerde.config(text="+")
    botonRosa= Button(seccion3, text= "Nuevo", bg="#F7089c")
    botonRosa.configure(height=3,width=5)
    botonRosa.pack()
    


#son clases las de arriba
#una libreria esta compuesta de muchas clases
#1. Creamos la ventana

Ventana = Tk() # Instancia para la clase TK, uso de poo, creando un obj ventana
Ventana.title("Ejemplo con 3 Frames")
Ventana.geometry("600x400")

#como crear un elemento vacio

#2. colocar las secciones de la ventana
seccion1 = Frame(Ventana, bg= "red")
seccion1.pack(expand=True, fill='both')

seccion2 = Frame(Ventana, bg= "green")
seccion2.pack(expand=True, fill= 'both')

seccion3 = Frame(Ventana, bg= "Black")
seccion3.pack(expand=True, fill='both')

#3. agregar, posicionar botones
#place
# hicimos un boton el cual le asignamos un texto dentro del boton, un lugar dentro de la ventana
#gracias a las coordenadas poniendole tamaño de altura y anchura.


#place
#Por medio de cordenadas
botonAzul= Button(seccion1, text= "Azul", fg= "#0733f7")
botonAzul.place(x=60,y=70, width=100, height=30)

#grid
#Por medio de filas y columnas
botonNegro= Button(seccion2, text= "Negrito", fg= "#292524", bg="#EC3636")
botonNegro.configure(height=2,width=10)
botonNegro.grid(row=0,column=1)

#Se le agrega el command= para que haga caso a lo que queremos ejecutuar al momento de usar ese boton
botonAmarillo= Button(seccion2, text= "Amarillo", bg="#DFCD33", command=mostrarMesaje)
botonAmarillo.configure(height=2,width=10)
botonAmarillo.grid(row=1,column=1)


#pack
#Automaticamente los coloca, uno debajo del otro siempre que sigamos creando
botonVerde= Button(seccion3, text= "Verde", bg="#06e813", command=addbtn)
botonVerde.configure(height=2,width=10)
botonVerde.pack()


botonVerde= Button(seccion3, text= "Verde2", bg="#06e813")
botonVerde.configure(height=2,width=10)
botonVerde.pack()



#Para que se ejecute, metodo
Ventana.mainloop()

