# Escribir un programa que almacene la cadena de caracteres una contraseña en
# una variable, después que solicite al usuario una contraseña e imprima en
# pantalla si la contraseña introducida por el usuario coincide con la guardada en
# la variable sin tener en cuenta mayúscula y minúscula.

password = input("Crea una contraseña: ")

repite = input("Escribe nuevamente la contraseña: ")

if password == repite:
    print("Es correcta tu contraseña")
else: 
    print("La contraseña es incorrecta")
    
    
