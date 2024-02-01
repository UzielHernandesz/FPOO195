# Escriba un programa que administre una cuenta bancaria, usando una bitácora
# de operaciones. (img 2)
# La bitácora de operaciones tiene la siguiente forma:
# D 100
# R 50
# D 100 significa que depositó 100 pesos
# R 50 significa que retiró 50 pesos
# Introducir una línea vacía indica que ha finalizado la bitácora e imprime el saldo
# final
saldo = 0

transacciones = int(input("Escribe el numero de operaciones a realizar:  "))

for i in range (transacciones):
    operacion = input("Escribe la operacion (D/R): ")
    cantidad = int(input("Escribe la cantidad: "))
    if operacion == "D":
        saldo += cantidad
    elif operacion == "R":
        saldo -= cantidad
    else:
        print("Operacion invalida")
        break
    print(f"")
    print(f"El saldo es: {saldo}")
    
    print(f"las transacciones son: {operacion}  {cantidad}")