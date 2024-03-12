    
class Persona:
    def __init__(self):
        self.__lista = []

    # Creamos los métodos
    def Insertar(self,nom):
        self.__lista.append({ "Nombre": nom})

    def consultar(self):
        print(self.__lista)

    def buscarUsuario(self, id):
        for usuario in self.__lista:
            if usuario['Id'] == id:
                print(usuario)
                return
        print("Usuario no encontrado")

    def eliminar(self, id):
        for usuario in self.__lista:
            if usuario['Id'] == id:
                self.__lista.remove(usuario)
                print(":: Usuario Eliminado ::")
                self.consultar()

    def editar(self, id, nom, edad):
        for usuario in self.__lista:
            if usuario['Id'] == id:
                usuario['Nombre'] = nom  
                usuario['Edad'] = edad  
                print(":: Usuario Editado ::")
                self.consultar()
                
    def validarUsuario(self,nombre,password):
        acceso = False
        for usuario in self.__lista:
            if usuario['Nombre']==nombre and usuario ['Passw'] == password :
                acceso = True 
                break 
        return acceso

    
    