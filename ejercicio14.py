#Crea una clase llamada CuentaBancaria con atributos titular y saldo. Agrega métodos para
#depositar y retirar dinero de la cuenta.
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a depositar debe ser mayor que 0.")
        else:
            self.saldo += cantidad
            print(f"Has depositado {cantidad} €. Saldo actual: {self.saldo} €")

    def retirar(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a retirar debe ser mayor que 0.")
        elif cantidad > self.saldo:
            print("No tienes suficiente saldo para realizar esta retirada.")
        else:
            self.saldo -= cantidad
            print(f"Has retirado {cantidad} €. Tu saldo restante es {self.saldo} €")


cuenta = CuentaBancaria("Pepe", 1000)

cuenta.depositar(500)
cuenta.retirar(200)
cuenta.retirar(2000)