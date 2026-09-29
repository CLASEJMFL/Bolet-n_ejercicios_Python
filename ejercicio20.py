# 20. Crea una clase base llamada Empleado con
# atributos nombre y salario, y un método
# calcular_salario_anual que calcule el salario anual
# del empleado. Luego, crea clases derivadas como
# Gerente y Programador que hereden de Empleado
# y añadan atributos y métodos específicos de cada
# tipo de empleado.

class Empleado:
    def __init__(self,nombre,salario):
        self.nombre = nombre
        self.salario = salario
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Salario: {self.salario}"
        
    def calcularSalarioAnual(self):
        anual = self.salario*12
        print("El salario anual de ",self.nombre," es de ",anual)
    
class Gerente(Empleado):
    def __init__(self, nombre, salario,departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento
        
    def depart(self):
        print("El gerente: ",self.nombre,", esta en el departamento: ",self.departamento)
        
class Programador(Empleado):
    def __init__(self, nombre, salario,lenguajePrincipal):
        super().__init__(nombre, salario)
        self.lenguajePrincipal = lenguajePrincipal
    def lenguaje(self):
        print("El gerente:",self.nombre,",esta en el departamento: ",self.lenguajePrincipal)


#Empleado:
e1 = Empleado("Paco",1200)
print(e1)
e1.calcularSalarioAnual()
print("===========================================")
#Gerente:
g1 = Gerente("Alvaro",2400,"Ventas")
print(g1)
g1.depart()

print("===========================================")
#Programador:
p1 = Programador("Juan",1900,"SQL")
print(p1)
p1.lenguaje()

