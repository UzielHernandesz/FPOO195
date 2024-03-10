import tkinter as tk
from tkinter import messagebox
import string
import random
#Inicialiamos nuestra clase
class PasswordGenerator:
    def __init__(self, length=8, include_uppercase=False, include_special_chars=False):
        self.length = length
        self.include_uppercase = include_uppercase
        self.include_special_chars = include_special_chars

#Metodo para generar nuestra contraseña, basasa en nuestros atributos 
    def generate_password(self):
        characters = string.ascii_letters + string.digits
        if self.include_uppercase:
            characters += string.ascii_uppercase
        if self.include_special_chars:
            characters += string.punctuation

        try:
            password = ''.join(random.choice(characters) for _ in range(self.length))
            return password
        except Exception as e:
            raise RuntimeError(f"Error al generar la contraseña: {str(e)}")

#Inicliaremos nuestra clase dgeneradora de contraseñas en nuestra ventana de tkinter
class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Contraseñas")
        self.root.geometry("400x300")

        self.password_generator = PasswordGenerator() #Nuestra instancia de la clase PasswordGenerator 

        self.setup_gui()

    def setup_gui(self):
        #Nuestra configuracion de nuestra interfaz donde vamos a incluir botones y etiquetas
        self.length_label = tk.Label(self.root, text="Longitud:")
        self.length_label.pack(pady=5)

        self.length_entry = tk.Entry(self.root)
        self.length_entry.insert(0, str(self.password_generator.length))
        self.length_entry.pack(pady=5)

        self.uppercase_var = tk.IntVar()
        self.uppercase_checkbox = tk.Checkbutton(self.root, text="Incluir Mayúsculas", variable=self.uppercase_var)
        self.uppercase_checkbox.pack(pady=5)

        self.special_chars_var = tk.IntVar()
        self.special_chars_checkbox = tk.Checkbutton(self.root, text="Incluir Caracteres Especiales", variable=self.special_chars_var)
        self.special_chars_checkbox.pack(pady=5)

        self.strength_button = tk.Button(self.root, text="Comprobar Fortaleza", command=self.check_strength)
        self.strength_button.pack(pady=10)

        self.generate_button = tk.Button(self.root, text="Generar Contraseña", command=self.generate_and_display_password)
        self.generate_button.pack(pady=10)

        self.password_entry = tk.Entry(self.root, show="*")  # Entry para mostrar la contraseña generada
        self.password_entry.pack(pady=10)

    def generate_and_display_password(self):
        # Método para generar y mostrar la contraseña en la interfaz y en un MessageBox
        self.password_generator.length = int(self.length_entry.get())
        self.password_generator.include_uppercase = bool(self.uppercase_var.get())
        self.password_generator.include_special_chars = bool(self.special_chars_var.get())

        try:
            password = self.password_generator.generate_password()
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)
            messagebox.showinfo("Contraseña Generada", f"Contraseña generada con éxito:\n{password}")
        except RuntimeError as e:
            messagebox.showerror("Error", str(e))

    def check_strength(self):
        
        messagebox.showinfo("Comprobar Fortaleza", "Funcionalidad no implementada aún.")

if __name__ == "__main__":
    #Aqui creamos nuestra ventana principal de nuestra instancia 
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
