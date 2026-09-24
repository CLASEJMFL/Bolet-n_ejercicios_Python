# 12. Luego, crea un objeto de tipo Persona e imprime sus atributos.

class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"
        
p1 = persona("Pepe", 60)
p2 = persona("María", 30)

print (p1)
print (p2)

