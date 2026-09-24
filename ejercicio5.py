# 5. Calcula el factorial de un número.

numero = int(input("Dame el numero que quieres sacar el factorial: "))
factorial = 1
contador = 1
while contador <= numero:
    factorial = factorial * contador
    contador += 1
    
print("Tu factorial es : ", factorial)