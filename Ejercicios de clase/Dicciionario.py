Datos_Basicos = {
    "Nombres": "Juan Carlos",
    "Apellidos": "Perez Garcia",
    "Dui": "01025487-9",
    "Fecha_Nacimiento": "1990-01-01",
    "Lugar_nacimiento": "Soya City",
    "nacionalidad": "salvadoreño",
    "Estado_civil": "Complicado"
}


print("Detalles del Diccionario")
print("Datos Basicos")

print("Claves del diccionario: ", Datos_Basicos.keys())
print("Valores del diccionario: ", Datos_Basicos.values())
print("Elementos del diccionario: ", Datos_Basicos.items())

print("Inscripcion del curso")
print("...........")

print("Inscripcion del participante")
print("...........")

print("DUI:", Datos_Basicos["Dui"])
print("Nombre Completo: ", Datos_Basicos["Nombres"] + " " + Datos_Basicos["Apellidos"])