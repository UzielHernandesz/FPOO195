# PROGRAMA QUE SOLICITE UNA PALABRA Y QUE LA DESCOMPONGA EN LETRAS 

palabra = input("Ingrese la palabra a descomponer: ")

for letra in [palabra]:
    
    if palabra == letra:

        print(f"La palabra descompuesta: {palabra}")
