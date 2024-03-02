from practica10 import*



print("=================CREAR USUARIO========")
id= int (input("Ingrese su id: "))
nombre = input("Ingrese el nombre de usuario: ")
apellp = input("Ingrese su apellido paterno: ")
apellm = input("Ingrese su apellido materno: ")
correo = input("Ingrese su correo: ")
contraseña = input("Ingrese su contraseña: ")


CrearUsuario (id,nombre,apellp,apellm,correo,contraseña)



print("============USUARIO CREADO==========")

print(CrearUsuario.get__id())
print(CrearUsuario.get__nombre())
print(CrearUsuario.get__apellp())
print(CrearUsuario.get__apellm())
print(CrearUsuario.get__correo())
print(CrearUsuario.get__contraseña())
print("")
