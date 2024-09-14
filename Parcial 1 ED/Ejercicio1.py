#Crea un progrma que almacene en una lista 5 números primos#
# y luego los imprima en pantalla.#
# Los números primos son los números naturales mayores que 1 que no tienen otros divisores
# que 1 y ellos mismos.

#nombre: Javier Eulices Martínez Martínez

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def crear_lista_primos():
    lista_primos = []
    num_primos = 0
    num = 2
    while num_primos < 5:
        if es_primo(num):
            lista_primos.append(num)
            num_primos += 1
        num += 1
    return lista_primos

lista_primos = crear_lista_primos()
print(lista_primos)
        