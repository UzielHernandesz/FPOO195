# Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase.

frase= input("Intrdoduzca una frase porfavor: ")
letra = input("Introduzca la letra que guste saber: ")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '{}' aparece {} veces en la frase '{}'.".format(letra, contador, frase))
