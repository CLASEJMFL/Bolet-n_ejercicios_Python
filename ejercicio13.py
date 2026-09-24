# 13. Crea una clase llamada Rectángulo con atributos ancho y altura. Agrega un método para calcular el área del rectángulo y otro para calcular su perímetro. 
ancho = 10
altura = 6

class Rectangulo:
    def __init__(self,ancho,altura):
        self.ancho = ancho
        self.altura = altura
    def area(self,ancho,altura):
        return "El area es " ((altura * ancho)*2)
        