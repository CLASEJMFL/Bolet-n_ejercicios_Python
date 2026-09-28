# 11. Crea una clase llamada Persona con atributos nombre y edad. 

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona(Nombre={self.nombre}, Edad={self.edad})"


p = Persona("Ana", 30)
print(p)