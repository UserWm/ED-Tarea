filas = int(input("ingrese el numero de filas: "))
columnas = int(input("ingrese el número de columnas: "))
matriz = []
print("Por favor, ingrese los valores de la matriz:")

for i in range(filas):
    fila = []
    for j in range(columnas):
        valor =  float(input(f"Elemento [{i+1}][{j+1}]: "))
        fila.append(valor)
        matriz.append(fila)
        
        print("La matriz ingresada es:")
        for fila in matriz:
            print(fila)