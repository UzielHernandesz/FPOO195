# Crea un programa que llene una lista de 30 valores aleatorios en un rango del 10
# al 20, con la lista llena el usuario podrá
# a. Contar número repetidos
# b. Eliminar numero repetidos
# c. Remplazar los repetidos con 0

import random

aleatorios = [random.randint(10, 20) for _ in range(30)]
print("Lista de números aleatorios es :", aleatorios)

while True:
    print("a. Contar números repetidos")
    print("b. Eliminar números repetidos")
    print("c. Reemplazar repetidos con 0")

    opcion = input("Seleccione la opcion que desee: ")

    if opcion == 'a':
        contar_repetidos = {}
        for num in aleatorios:
            contar_repetidos[num] = contar_repetidos.get(num, 0) + 1

        for num, cantidad in contar_repetidos.items():
            if cantidad > 1:
                print(f"El número {num} se repite {cantidad} veces.")

    elif opcion == 'b':
        aleatorios = list(set(aleatorios))
        print("Números repetidos eliminados:", aleatorios)

    elif opcion == 'c':
        contar_repetidos = {}
        for i in range(len(aleatorios)):
            if aleatorios[i] in contar_repetidos:
                aleatorios[i] = 0
            else:
                contar_repetidos[aleatorios[i]] = 1

        print("Asi quedo:", aleatorios)

