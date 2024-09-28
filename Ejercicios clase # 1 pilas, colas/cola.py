class cola:
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
       self.items.append(item)
       
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "La cola está vacía"
        
    def is_empty(self):
        return len(self.items) == 0
    
cola = cola()

cola.enqueue("Ulises")
cola.enqueue("Stacy")
cola.enqueue("Itamar")
cola.enqueue("Diego")

print("Pasar :", cola.dequeue())
print("Pasar :", cola.dequeue())
print("Pasar :", cola.dequeue())
print("Pasar :", cola.dequeue())
print("Pasar :", cola.dequeue())

print("El estado de la cola es :", cola.is_empty())