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
num_operaciones = int(input("Escriba el número de operaciones: "))
for _ in range(num_operaciones):
    s = input("Escriba la bitacora de operaciones: ")
    datos = s.split(" ")
    operacion = datos[0]
    monto = int(datos[1])
    if operacion == "D":
        saldo += monto
    elif operacion == "R":
        saldo -= monto
    else:
        pass

print(saldo)