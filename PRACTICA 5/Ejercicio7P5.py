# Imprime un árbol de navidad formado con Asteriscos haciendo uso del while,
# Solicitando al usuario la cantidad de * de la base (img 3)

base_arbol = int(input("Ingrese la cantidad de * que desea para su base: "))
z = base_arbol - 1
x = 1

while z >= 0:
    print(' ' * z + '*' * x + ' ' * z)
    x += 2
    z -= 1
