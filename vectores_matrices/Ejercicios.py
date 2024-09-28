# Javier Eulices Martínez Martínez

# Vectores

#Ejercicio 1.

vector = []
for i in range(5):
    num = int(input("Por favor, ingrese un número: "))
    vector.append(num)
    print("La suma de los elementos del vector es: ", sum(vector))
    

#Ejercicio 2.


promedio = [6, 7, 8, 7, 5, 6, 7, 8, 9, 10] 
promedio = sum(promedio) / len(promedio)
print("El promedio de los valores ingresados es: ", promedio)


#Ejercicio 3.


mayor = 0
for i in range(7):
    num = int(input("Por favor, ingrese un número: "))
    if num > mayor:
        mayor = num
        print("El mayor de los números ingresados es: ", mayor)
        
#Ejercicio 4.
     

positivos = 0
for i in range(8):
    num = int(input("Por favor, ingrese un número: "))
    if num > 0:
        positivos += 1
        print("La cantidad de números positivos ingresados es: ", positivos)
        
        
#Ejercicio 5

 
vector = [1, 2, 3, 4, 5, 6]
vector_invertido = vector[::-1]
print(vector_invertido)



#Ejercicio 1  
matriz_identidad = []
 
for i in range(3):
    fila = []
    for j in range(3):
        if i == j:
            fila.append(1)  
        else:
            fila.append(0)   
    matriz_identidad.append(fila)   

 
for fila in matriz_identidad:
    print(fila)



#Ejercicio 2



 
matriz_identidad = []
 
for i in range(4):
    fila = []
    for j in range(4):
        if i == j:
            fila.append(1)  
        else:
            fila.append(0)   
    matriz_identidad.append(fila)   

 
for fila in matriz_identidad:
    print(fila)
    

#Ejercicio 3


matriz = []

 
for i in range(2):
    fila = []
    for j in range(3):
        num = float(input(f"Ingrese el elemento en la posición [{i+1}, {j+1}]: "))
        fila.append(num)
    matriz.append(fila)

 
matriz_transpuesta = []
for j in range(3):  
    fila_transpuesta = []
    for i in range(2):   
        fila_transpuesta.append(matriz[i][j])
    matriz_transpuesta.append(fila_transpuesta)

 
print("La matriz transpuesta es:")
for fila in matriz_transpuesta:
    print(fila)

        
#Ejercicio 4 

 
matriz1 = []
matriz2 = []

 
print("Ingrese los elementos para la primera matriz:")
for i in range(2):
    fila = []
    for j in range(2):
        num = float(input(f"Ingrese el elemento en la posición [{i+1}, {j+1}] de la primera matriz: "))
        fila.append(num)
    matriz1.append(fila)

 
print("Ingrese los elementos para la segunda matriz:")
for i in range(2):
    fila = []
    for j in range(2):
        num = float(input(f"Ingrese el elemento en la posición [{i+1}, {j+1}] de la segunda matriz: "))
        fila.append(num)
    matriz2.append(fila)

 
resultado = [[0, 0], [0, 0]]

 
for i in range(2):
    for j in range(2):
        resultado[i][j] = (matriz1[i][0] * matriz2[0][j] +
                           matriz1[i][1] * matriz2[1][j])

 
print("La matriz resultado de la multiplicación es:")
for fila in resultado:
    print(fila)
    
    


#Ejercicio 5
matriz = []


for i in range(3):
    fila = []
    for j in range(3):
        num = float(input(f"Ingrese el elemento de la posición [{i+1}, {j+1}] de la matriz: "))
        fila.append(num)
    matriz.append(fila)  

 
print("Los elementos de la diagonal principal son:")
for i in range(3):
    print(matriz[i][i], end=" ")
print()                          