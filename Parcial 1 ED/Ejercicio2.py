#solicita 10 números al usuario y almacena en una lista solo los números impares#
#nombre: Javier Eulices Martínez Martínez
numeros = []
for i in range(10):
    num = int(input(f"ingrese el número {i+1}: "))
    if num % 2 != 0:
        numeros.append(num)
print("Lista de números impares:", numeros)           