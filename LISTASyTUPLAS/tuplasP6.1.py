# Programa los siguientes Ejercicios
# a. Crea un programa usando funciones y lo que necesites para que el usuario inserte
# N números en una Tupla, después de la captura debe desplegar el siguiente menú
# funcional
# 1. Sumatoria de los elementos de la lista
# 2. Numero mayor de la lista
# 3. Numero menor de la lista
# 4. Promedio
# 5. Moda: es el valor que más se repite de un conjunto de datos
# 6. Rango: es la diferencia entre el valor máximo y el valor mínimo de un
# conjunto de datos

def main():
    numeros = input("Ingrese los numeros deseados: ")
    lista = convertir_a_lista(numeros)
    tupla = convertir_a_tupla(lista)
    
    print("1.Sumatoria")
    print("2.Número Mayor")
    print("3.Número Menor")
    print("4.Promedio")
    print("5.Moda")
    print("6.Rango")

    opcion = int(input("Ingrese la opción deseada: ").strip())


    if opcion == 1:
        mostrar(sumatoria(tupla))
    elif opcion == 2:
        mostrar(numero_mayor(tupla))
    elif opcion == 3:
        mostrar(numero_menor(tupla))
    elif opcion == 4:
        mostrar(promedio(tupla))
    elif opcion == 5:
        mostrar(moda(tupla))
    elif opcion == 6:
        mostrar(rango(tupla))

def convertir_a_lista(numeros):
    return [int(numero) for numero in numeros.split(",")]

def convertir_a_tupla(lista):
    return tuple(lista)

def sumatoria(tupla):
    return sum(tupla)

def numero_mayor(tupla):
    return max(tupla)

def numero_menor(tupla):
    return min(tupla)

def promedio(tupla):
    return sum(tupla) / len(tupla)

def moda(tupla):
    return max(set(tupla), key=tupla.count)

def rango(tupla):
    return max(tupla) - min(tupla)

def mostrar(resultado):
    print(resultado)
if __name__ == "__main__":
    main()
