# 17. Crea una clase base llamada FiguraGeometrica
# con atributos ancho y altura, y un método area que
# calcule el área de la figura. Luego, crea clases
# derivadas como Rectangulo y Triangulo que
# hereden de FiguraGeometrica y sobrescriban el
# método area para calcular el área específica de
# cada figura.

class FiguraGeometrica:
    def __init__(self,ancho,altura):
        self.ancho = ancho
        self.altura = altura

class rectangulo(FiguraGeometrica):
    def areaRectangulo(self):
        area = self.ancho*self.altura
        print("El area del rectangulo es",area)
    
    
class triangulo(FiguraGeometrica):
    def areaTriangulo(self):
        area = (self.ancho*self.altura)/2
        print("El area del triangulo es",area)
    
t1 = triangulo(10,15)
r1 = rectangulo(15,8)

t1.areaTriangulo()
r1.areaRectangulo()
    