# 13. Crea una clase llamada Estudiante con atributos
#nombre, edad y curso. Crea varios objetos de tipo
#Estudiante y almacénalos en una lista. Luego, itera
#sobre la lista e imprime la información de cada
#estudiante.

lista_nombre=[]
lista_edad=[]
lista_curso=[]       
class Estudiante:
    def __init__(self,nombre,edad,curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso   
        lista_nombre.append(self.nombre)
        lista_edad.append(self.edad)
        lista_curso.append(self.curso)
        
e1 = Estudiante("Paco",25,"2ºDAW")
e2 = Estudiante("Pepe",20,"2ºASIR")
e3 = Estudiante("Maria",32,"2ºDAM")
e4 = Estudiante("Ana",22,"1ºDAW")
e5 = Estudiante("Pedro",21,"1ºASIR")

for i in range(len(lista_nombre)):
    print("El estudiante ",lista_nombre[i]," tiene ",lista_edad[i]," años y esta en el curso ",lista_curso[i])     