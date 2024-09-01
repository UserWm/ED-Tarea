temperaturas = [
                23.5, 24.0, 22.8, 25.1, 23.3, 24.8, 22.5, 25.0, 23.7, 24.2
]

while True:
    opción = input("¿ver alguna temperatura especifica (si/no):").strip().lower()
    if opción == "si":
        posicion = int(input("ingrese la posicion (1-10) de la temperatura que deseas ver: "))
        if 1 <= posicion <=10:
            print(f"La temperatura en la posicion {posicion} es: {temperaturas[posicion -1]:.2f}")
        else:
            print("Posición fuera de rango. Por favor, ingrese un número entre 1 y 10. ")
            print("Posicion fuera de rango. Por favor, ingrese un numero entre 1 y 10. ")
    elif opción == "no":
        print("cierre el programa.")
        break 

    else:
        print("Por favor, ingresa 'si' o 'no'.")
        
        