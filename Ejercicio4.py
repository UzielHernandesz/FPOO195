# Codifica un programa que pregunte el nombre del usuario y después de que el
# usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde
# <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras
# que tienen el nombre.

var1= input("introduce tu nombre compelto:")
print("Nombre completo es:",var1)
print("Nombre completo en mayúsculas:", var1.upper())
total_letras = len(var1)
print ("El total de letras en el nombre es:",total_letras)
