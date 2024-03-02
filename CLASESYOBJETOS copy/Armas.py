class Armas:
    
    def seleccionar_arma(self,get__nombre):
        seleccion = int (input("Selecciona el arma:\n 1=Rifle de asalto\n 2= Espada energia\n 3= Rifle M392"))
        
        if(seleccion== 1):
            print("Rifle de asalto asignado a " + get__nombre())
            print("Municiones 7.62 * 52mm, sin mira ")
            
        if(seleccion ==2):
            print("Espada de energia asignada a " + get__nombre())
            print("Arma creada por los Shagheili")
        
        if(seleccion == 3):
            print("Rifle M392 asignado a " + get__nombre())
            print("Municiones 7.62 * 52mm, con mira ")
            
            
            
    def Recargar_Arma(self, municion):
        cargador= 25
        cargador= cargador + municion
        print("Arma recargada al " + str(cargador) + "%")
        