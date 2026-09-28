# 12. Crea una clase llamada Rectangulo con atributos
# ancho y altura. Agrega un método para calcular el
# área del rectángulo y otro para calcular su
# perímetro.

class Rectangulo:
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura
        
    def area(self):
        return self.ancho * self.altura
        
    def perimetro(self):
        return (self.altura * 2) + (self.ancho * 2)
        
r1 = Rectangulo(12, 7)

print(r1.area())
print(r1.perimetro())