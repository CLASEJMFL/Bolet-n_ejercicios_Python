# 7. Calcula el máximo común divisor (MCD) de dos números. 
num1 = int(input("Dame el primer número: "))
num2 = int(input("Dame el segundo número: "))

MCD = 0

numMayor = 0
if num1 > num2:
    numMayor = num1
else:
    numMayor = num2

contador = 1

while contador <= numMayor:
    if (num1 % contador == 0) and (num2 % contador == 0):
        MCD = contador
    contador += 1

print("El máximo común divisor es:", MCD)