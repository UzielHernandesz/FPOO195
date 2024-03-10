import sys
from Persona import Persona
from Login import Login

objectPeople = Persona()
objectLogin = Login()

while True:
    print("==Menu==")
    print("1. Insertar usuario: ")
    print("2. Consultar usuario: ")
    print("3. Buscar usuario: ")
    print("4. Eliminar usuario: ")
    print("5. Editar usuario: ")
    print("6. Login")
    print("7. Salir")
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        print(" == Ingrese los datos del usuario ==")
        id = input("Escribe el Id:")
        nom = input("Escibre el Nombre: ")
        try:
            eda = int(input("Escriba la Edad: "))
        except ValueError:
            print("Error: La edad debe ser un número.")
            continue

        objectPeople.Insertar(id, nom, eda)
        print(" :: Persona Agregada correctamente ::")

    elif opcion == "2":
        print(" :: Estas son las personas guardadas ::")
        objectPeople.consultar()

    elif opcion == "3":
        print(" :: Introduce Id de la persona ::")
        id = input("Id: ")
        objectPeople.buscarUsuario(id)

    elif opcion == "4":
        print(" :: Introduce Id de la persona a eliminar ::")
        id = input("Id:")
        try:
            objectPeople.eliminar(id)
            print(":: Persona eliminada correctamente ::")
        except ValueError:
            print("Error: La persona con el Id especificado no existe.")

    elif opcion == "5":
        print(":: Introduce Id de la persona a editar ::")
        id = input("Id:")
        nm = input("Nombre: ")
        try:
            ed = int(input("Edad: "))
        except ValueError:
            print("Error: La edad debe ser un número.")
            continue
        objectPeople.editar(id, nm, ed)

    elif opcion == "6":
        status = objectLogin.crearLogin(objectPeople)

    elif opcion == "7":
        print("Bye!! ")
        sys.exit()

    else:
        print("Opción no válida. Por favor, elige una opción válida.")

