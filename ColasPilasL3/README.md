# Eliminación de Elemento en Cola con Recursión en Python

### Descripción del Programa

Este programa implementa una solución recursiva en Python para eliminar un elemento específico de una cola sin utilizar estructuras de datos auxiliares. Utilizando la estructura `deque` del módulo `collections`, el programa elimina todas las apariciones de un dato determinado y luego restaura el orden original de los elementos, ya que el proceso recursivo invierte la secuencia durante la eliminación.

## Funcionamiento del Programa

El programa se compone de dos funciones recursivas:

- **`eliminarElemento(cola, dato)`**:  
  Recorre la cola recursivamente, extrayendo el primer elemento y, tras procesar el resto de la cola, vuelve a insertar el elemento si no coincide con el dato a eliminar.

- **`ordenar(cola)`**:  
  Restaura el orden original de la cola extrayendo y reinsertando los elementos de forma recursiva, contrarrestando la inversión generada durante la eliminación.

El flujo del programa es el siguiente:
1. Se crea una cola y se llena con elementos (en este ejemplo, los números del 1 al 6 repetidos varias veces).
2. Se muestra la cola original.
3. Se elimina el elemento especificado (en este caso, el número 3).
4. Se restaura el orden original de la cola.
5. Se muestra la cola resultante.

## Código Fuente

```python
from collections import deque

def eliminarElemento(cola: deque, dato: int):
    # Caso base: si la cola está vacía, termina la recursión.
    if not cola:
        return
    
    frente = cola.popleft()
    
    eliminarElemento(cola, dato)
    
    if frente != dato:
        cola.append(frente)

def ordenar(cola: deque):
    # Caso base: si la cola está vacía, termina la recursión.
    if not cola:
        return
    
    frente = cola.popleft()
    
    ordenar(cola)
    cola.append(frente)

def main():
    cola = deque()
    
    for num in [1, 2, 3, 4, 5, 6] * 5:
        cola.append(num)
    
    datoAEliminar = 3
    print("Cola original:", list(cola))
    
    eliminarElemento(cola, datoAEliminar)
    ordenar(cola)
    
    print("Cola después de eliminar", datoAEliminar, ":", list(cola))

if __name__ == '__main__':
    main()
```

# Conclusión:
Este programa demuestra cómo se puede aplicar la recursión para manipular una estructura de datos simple en Python sin recurrir a estructuras auxiliares. 
