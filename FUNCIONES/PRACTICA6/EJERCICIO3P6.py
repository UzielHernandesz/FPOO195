# Escribir una función que convierta un número decimal en binario y
# otra que convierta un número binario en decimal.

def numero_decimal_a_numero_bi(decimal):
    
    return bin(decimal)[2:]
def bi_a_decimal(binario):
    
    return int(binario, 2)

numero_decimal = int(input("Ingrese su numero decimal: "))

print(f"El numero en binario es: {numero_decimal_a_numero_bi(numero_decimal)}")

numero_binario = input("Ingrese su numero binario: ")

print(f"El numero decimal equivalente es: {bi_a_decimal(numero_binario)}")
