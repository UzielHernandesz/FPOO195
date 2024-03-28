from tkinter import messagebox
import sqlite3 
import bcrypt
class Controlador:
    def conexion(self):
        try:
            conex = sqlite3.connect("C:/Users/Uziel/OneDrive/Documentos/REPOSITORIO GIT/FPOO195/tkSQLite/db195.db")
            print("Conectado")
            return conex
        except sqlite3.OperationalError:
            print("No se pudo conectar")

    def encriptapass(self, cont):
        passPlana = cont.encode()
        sal = bcrypt.gensalt()
        passHash = bcrypt.hashpw(passPlana, sal)
        return passHash

    def insertUsuario(self, nom, corr, cont):
        conexion = self.conexion()
        if (nom == "" or corr == "" or cont == ""):
            messagebox.showwarning("Cuidado", "Inputs vacíos")
            conexion.close()
        else:
            
            cursor = conexion.cursor()
            conH = self.encriptapass(cont)
            datos = (nom, corr, conH)
            sqlinsert = "INSERT INTO usuarios(nombre, correo, contra) VALUES (?, ?, ?)"
            
            cursor.execute(sqlinsert, datos)
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Éxito", "Registro exitoso!")
        
    def buscarUsuario(self, id_usuario):
        conexion = self.conexion()
        cursor = conexion.cursor()
    
        sqlconsulta = "SELECT id, nombre, correo, contra FROM usuarios WHERE id = ?"
        cursor.execute(sqlconsulta, (id_usuario,))

        usuario = cursor.fetchone()
        conexion.close()
        if usuario:
        
            print("Usuario:", usuario)
            return usuario
        else:
            messagebox.showwarning("Error", "Ese usuario no existe tibio.")
            return None
    
    #consultar todos           
    def consultarTodosUsuarios(self):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            sqlSelect = "select * from usuarios"
            cursor.execute(sqlSelect)
            usuarios = cursor.fetchall()
            conexion.close()
            return usuarios
        
        except sqlite3.OperationalError:
            print("Error de tu consulta tibio")
        
        
    # def buscarUsuario(self, id):
    #     conex= self.conexion()
    #     usuario= cursor.fetchone()
        
    #     if(id== ''):
    #         messagebox.showwarning("Cuidado", "Inputs vacíos")
    #         conex.close()
            
    #     else: 
    #         print("Usuario", usuario)
            #try:
            #   cursor = conex.cursor()
            #     sqlSelect= "select * from usuarios where id="+id
            #     cursor.execute(sqlSelect)
            #     usuario= cursor.fetchall()
            #     conex.close()
            #     return usuario
            # except sqlite3.OperationalError:
            #     print("No se pudo ejecutar la busqueda")
    