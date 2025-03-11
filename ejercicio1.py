from queue import Queue

def elim_dato(cola, dato, elim=False):
    if cola.empty():
        return cola

    elemento = cola.get()

    if elemento == dato and not elim:
        elim = True
        return elim_dato(cola, dato, elim)
    else:
        nueva_cola = elim_dato(cola, dato, elim)
        nueva_cola.put(elemento)
        return nueva_cola


cola = Queue(5)
cola.put(10)
cola.put(20)
cola.put(30)
cola.put(40)
cola.put(50)

print("Cola original:")
print(list(cola.queue))

cola = elim_dato(cola, 30)

print("Cola luego de eliminar la primera ocurrencia del dato:")
print(list(cola.queue))

