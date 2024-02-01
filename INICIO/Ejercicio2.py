# Codifica un programa que pregunte el nombre completo del usuario en la consola y
# después muestre por pantalla el nombre completo del usuario tres veces, una con
# todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la
# primera letra del nombre y de los apellidos en mayúscula. El usuario puede
# introducir su nombre combinando mayúsculas y minúsculas como quiera.

var1= input("introduce tu nombre:")
var2= input("introduce tu apellido:")
print("Nombre en minúsculas:", var1.lower())
print("Nombre en mayúsculas:", var2.upper())
print("Primeras letras:",  var1[0:1],var2)







