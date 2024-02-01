# 1. Escribir una función que calcule el total de una factura tras aplicarle
# el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de
# IVA a aplicar, y devolver el total de la factura. Si se invoca la función
# sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

cantidad= int(input("Ingrese la cantidad sin IVA: "))
iva= int(input("Ingrese iva a calcular: "))
def total_con_iva(cantidad, iva):
    total= cantidad * iva
    return total

print(f"La factura con el iva ingresado sera de: ")
print(f"")
