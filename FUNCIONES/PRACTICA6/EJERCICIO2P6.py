# Escribir una función que calcule el área de un círculo y otra que
# calcule el volumen de un cilindro usando la primera función.

# import math

# def area_circulo_deseado(radio):
#     return math.pi * radio **2

# def volumen_cilindro(radio, altura):
#     return area_circulo_deseado(radio) * altura
# radio_circulo_deseado = float(input("Ingrese el radio de su circulo: "))
# altura_cilindro= float(input("Ingrese la altura del cilindro: "))

# print(f"El area del cilindro es: {area_circulo_deseado(radio_circulo_deseado)}")
# print(f"El volumen del cilindro es: { volumen_cilindro(radio_circulo_deseado, altura_cilindro)}")




def area_circulo_deseado(radio):
    return 3.1416 * radio **2

def volumen_cilindro(radio, altura):
    return area_circulo_deseado(radio) * altura
radio_circulo_deseado = float(input("Ingrese el radio de su circulo: "))
altura_cilindro= float(input("Ingrese la altura del cilindro: "))

# decimales_mostrar = 2


print(f"El area del cilindro es: {area_circulo_deseado(radio_circulo_deseado)}")
print(f"El volumen del cilindro es: { volumen_cilindro(radio_circulo_deseado, altura_cilindro)}")
