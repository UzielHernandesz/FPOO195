# 1. Escribir una función que calcule el total de una factura tras aplicarle
# el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de
# IVA a aplicar, y devolver el total de la factura. Si se invoca la función
# sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

# cantidad= int(input("Ingrese la cantidad sin IVA: "))
# iva= int(input("Ingrese iva a calcular: "))
# def total_con_iva(cantidad, iva):
#     total= cantidad * iva
#     return total

# print(f"La factura con el iva ingresado sera de: ")
# print(f"")

def factura(sin_iva, porcentaje_iva= 21):
    total= sin_iva + (sin_iva * porcentaje_iva / 100)
    return total

sin_iva = float(input("Ingrese la cantidad sin IVA:  "))
porcentaje_iva_usuario = input("Ingrese el porcentaje de IVA:")

if porcentaje_iva_usuario:
    porcentaje_iva = float(porcentaje_iva_usuario)
else:
    porcentaje_iva = 21
total= factura(sin_iva, porcentaje_iva)
print("El total de la factura es: ", total)