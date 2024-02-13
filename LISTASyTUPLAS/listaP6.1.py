# Crea un programa que llene una lista de 30 valores aleatorios en un rango del 10
# al 20, con la lista llena el usuario podrá
# a. Contar número repetidos
# b. Eliminar numero repetidos
# c. Remplazar los repetidos con 0





import random
from collections import Counter

print("Ingrese el numero de valores")
n=int(input())
aleatorios = [random.randint(10,20) for _ in range(n)]
print(aleatorios)

lista = [n]
contador = Counter(lista)
print(contador)

