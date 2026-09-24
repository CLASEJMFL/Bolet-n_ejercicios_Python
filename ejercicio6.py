# 6. Verifica si un número es par o impar. 
numero = int(input("Dame el numero que quieres comprobar si es par o impar: "))

comprobador = (numero%2)
if comprobador == 0:
    print ("Su numero es par")
else :
    print ("Su numero es impar")