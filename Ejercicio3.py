# Escribir un programa que solicite un entero X, introducido por el usuario y después
# muestre en pantalla la suma de todos los enteros desde 1 hasta X .


var1 = int(input("Introduce un número entero X: "))
suma = 0

suma_total = sum(range(1, var1 + 1))

print(f"La suma de los enteros desde 1 hasta {var1} es: {suma_total}")
