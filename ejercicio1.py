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


# Readme.md

# Ejercicio 1
### Enunciado
# # 1. Eliminar elemento.
# Escriba una función que reciba como parámetro una cola y un dato. La función debe:
# 1. Eliminar el dato de la cola
# 2. Mostrar por consola la cola con lados en el orden de llegada luego de eliminar el dato.
# 3. La función no debe declarar una estructura de datos dinámica o estática auxiliar para
# eliminar el dato de la cola.

### Solución
