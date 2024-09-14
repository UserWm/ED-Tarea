#Solicita ala usuario llenar una matriz de 5x5 donde solo se llene de números primos#
#nombre: Javier Eulices Martínez Martínez
def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

matriz = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    for j in range(5):
        while True:
            try:
                num = int(input(f"Ingrese un número primo para la posición [{i}][{j}]: "))
                if es_primo(num):
                    matriz[i][j] = num
                    break
                else:
                    print("El número ingresado no es primo")
            except ValueError:
                print("Por favor, ingrese un número válido")           