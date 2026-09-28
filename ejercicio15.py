#15. Crea una clase llamada Coche con atributos
#marca y modelo. Crea un método que imprima la
#información del coche en un formato legible.

class Coche:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
    
    def __str__(self):
        return f"La marca es {self.marca} y el modelo es {self.modelo}"

c1 = Coche("Citroen","C3")

print(c1)