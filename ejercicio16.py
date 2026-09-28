# 16. Crea una clase base llamada Animal con un
# método hablar que imprima un mensaje genérico.
# Luego, crea dos clases derivadas, Perro y Gato,
# que hereden de Animal y sobrescriban el método
# hablar para imprimir mensajes diferentes.

class Animal:
    def hablar(self):
        print("Este animal emite un sonido genérico.")

class Perro(Animal):
    def hablar(self):
        print("El perro hace: ¡Guau, guau!")
class Gato(Animal):
    def hablar(self):
        print("El gato hace: ¡Miau, miau!")

mi_animal = Animal()
mi_perro = Perro()
mi_gato = Gato()

mi_animal.hablar()  
mi_perro.hablar()   
mi_gato.hablar()    
