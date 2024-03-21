class Cuenta:
    
    
    def __init__(self, numero_cuenta, titular, edad, saldo):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.edad = edad
        self.saldo = saldo


    def ingresar_efectivo(self, cantidad):
        self.saldo += cantidad
    
    
    def consultar_saldo(self):
        return self.saldo
    
    
    def retirar_efectivo(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        else:
            return False
    
    def depositar_otra_cuenta(self, otra_cuenta, cantidad):
        if self.retirar_efectivo(cantidad):
            otra_cuenta.ingresar_efectivo(cantidad)
            return True
        else:
            return False
