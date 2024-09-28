class Pila:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "La pila está vacía"
        
    def is_empty(self):
        return len(self.items) == 0
    
    def zise(self):
        return len(self.items)
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "La pila está vacía"

# Crear una instancia de la clase Pila
pilaTeléfono = Pila()

pilaTeléfono.push(10)
pilaTeléfono.push(20)
pilaTeléfono.push(30)
pilaTeléfono.push(40)
pilaTeléfono.push(50)

# Verificar si la pila está vacía
#print("La batería está vacía: ", pilaTeléfono.is_empty())
#print("Tamaño de la pila es: ", pilaTeléfono.zise())

print("Total de carga de la pila es: ", pilaTeléfono.peek())

print("Descargando batería: ", pilaTeléfono.pop())
print("Nuevo teléfono de la carga de la pila es: ", pilaTeléfono.peek())
print("La batería está vacía: ", pilaTeléfono.is_empty())

print("Descargando batería: ", pilaTeléfono.pop())
print("Nuevo teléfono de la carga de la pila es: ", pilaTeléfono.peek())
print("La batería está vacía: ", pilaTeléfono.is_empty())

print("Descargando batería: ", pilaTeléfono.pop())
print("Nuevo teléfono de la carga de la pila es: ", pilaTeléfono.peek())
print("La batería está vacía: ", pilaTeléfono.is_empty())

print("Descargando batería: ", pilaTeléfono.pop())
print("Nuevo teléfono de la carga de la pila es: ", pilaTeléfono.peek())
print("La batería está vacía: ", pilaTeléfono.is_empty())

print("Descargando batería: ", pilaTeléfono.pop())
print("Nuevo teléfono de la carga de la pila es: ", pilaTeléfono.peek())
print("La batería está vacía: ", pilaTeléfono.is_empty())
