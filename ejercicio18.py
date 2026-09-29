# 18. Crea una clase base llamada Vehiculo con
# atributos marca y modelo, y un método informacion
# que imprima la información del vehículo. Luego,
# crea clases derivadas como Coche y Bicicleta que
# hereden de Vehiculo y añadan atributos y métodos
# específicos de cada tipo de vehículo.
class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
    
    def __str__(self):
        return f"La marca es {self.marca} y el modelo es {self.modelo}"
    
    def informacion(self,velocidad,caballos,tanque):
        self.velocidad = velocidad
        self.caballos = caballos
        self.tanque = tanque
        
class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        
c1 = Vehiculo("Citroen","C3")
c1.informacion("188km/h","110cv","45L")

print(c1)