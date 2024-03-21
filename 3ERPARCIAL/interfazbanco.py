import tkinter
from tkinter import messagebox
from banco import Cuenta

def ingresar_efectivo():
    cantidad = float(caja1.get())
    cuenta_actual.ingresar_efectivo(cantidad)
    messagebox.showinfo("Éxito", f'Se han ingresado {cantidad} pesos. Nuevo saldo: {cuenta_actual.consultar_saldo()} pesos')

def retirar_efectivo():
    cantidad = float(caja1.get())
    exito = cuenta_actual.retirar_efectivo(cantidad)
    if exito:
        messagebox.showinfo("Resultado", f'Se han retirado {cantidad} pesos. Nuevo saldo: {cuenta_actual.consultar_saldo()} pesos')
    else:
        messagebox.showerror("Error", "Saldo insuficiente")

def depositar_cuenta():
    num_cuenta_destino = int(caja2.get())
    cantidad = float(caja1.get())
    if num_cuenta_destino in cuentas:
        cuenta_destino = cuentas[num_cuenta_destino]
        exito = cuenta_actual.depositar_otra_cuenta(cuenta_destino, cantidad)
        if exito:
            messagebox.showinfo("Resultado", f'Se han depositado {cantidad} pesos a la cuenta {num_cuenta_destino}. Nuevo saldo: {cuenta_actual.consultar_saldo()} pesos')
        else:
            messagebox.showerror("Error", "Saldo insuficiente")
    else:
        messagebox.showerror("Error", "La cuenta destino no existe")

def consultar_cuenta():
    num_cuenta = int(caja3.get())
    if num_cuenta in cuentas:
        saldo = cuentas[num_cuenta].consultar_saldo()
        titular = cuentas[num_cuenta].titular
        messagebox.showinfo("Consulta de Cuenta", f"El titular de la cuenta {num_cuenta} es: {titular}. El saldo de la cuenta es: {saldo} pesos.")
    else:
        messagebox.showerror("Error", "La cuenta especificada no existe")


cuenta1 = Cuenta(1, "Vargas_Uziel", 45, 100)
cuenta2 = Cuenta(2, "Loyola_Cris", 55, 300)

cuentas = {1: cuenta1, 2: cuenta2}
cuenta_actual = cuenta1

ventana = tkinter.Tk()
ventana.title("CajaPopular")
ventana.geometry("600x400")
ventana.configure(bg="#F0F0F0")

label_titulo = tkinter.Label(ventana, text="GUARDADITO AZTECA", font=("Helvetica", 25), bg="#F0F0F0")
label_caja1 = tkinter.Label(ventana, text="Cantidad $", font=("Helvetica", 12), bg="#F0F0F0")
label_caja2 = tkinter.Label(ventana, text="Número de cuenta destinatario", font=("Helvetica", 12), bg="#F0F0F0")
label_caja3 = tkinter.Label(ventana, text="Número de cuenta a consultar", font=("Helvetica", 12), bg="#F0F0F0")

caja1 = tkinter.Entry(ventana, font=("Helvetica", 15))
caja2 = tkinter.Entry(ventana, font=("Helvetica", 15))
caja3 = tkinter.Entry(ventana, font=("Helvetica", 15))

boton_ingresar = tkinter.Button(ventana, text="Ingresar dinero", bg="#4CAF50", fg="white", font=("Helvetica", 12), width=25, command=ingresar_efectivo)
boton_retirar = tkinter.Button(ventana, text="Retirar dinero", bg="#FF5733", fg="white", font=("Helvetica", 12), width=25, command=retirar_efectivo)
boton_depositar = tkinter.Button(ventana, text="Depositar dinero", bg="#007BFF", fg="white", font=("Helvetica", 12), width=25, command=depositar_cuenta)
boton_consultar_cuenta = tkinter.Button(ventana, text="Consultar cuenta", bg="#FFC300", fg="white", font=("Helvetica", 12), width=25, command=consultar_cuenta)

label_titulo.pack(pady=8)
label_caja1.pack(pady=5)
caja1.pack()
label_caja2.pack()
caja2.pack()
label_caja3.pack()
caja3.pack()

boton_ingresar.pack(pady=5)
boton_retirar.pack(pady=5)
boton_depositar.pack(pady=5)
boton_consultar_cuenta.pack(pady=5)

ventana.mainloop()
