# 19. Crea una clase base llamada InstrumentoMusical
# con un método tocar que imprima un mensaje
# genérico. Luego, crea clases derivadas como Piano
# y Guitarra que hereden de InstrumentoMusical y
# sobrescriban el método tocar para imprimir
# mensajes diferentes.

class InstrumentoMusical:
    def __init__(self, nombre):
        self.nombre = nombre

    def tocar(self):
        print("Estás tocando", self.nombre)
class Piano(InstrumentoMusical):
    def tocar(self):
        print("Estás tocando el piano muy mal")
class Guitarra(InstrumentoMusical):
    def tocar(self):
        print("Estás tocando la guitarra muy mal")


i1 = InstrumentoMusical("Instrumento")
piano = Piano("Piano")
guitarra = Guitarra("Guitarra")

i1.tocar()
piano.tocar()
guitarra.tocar()