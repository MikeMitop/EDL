# Eliminación de Elemento.

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

# --------------------------------------------------------------------------------------


# Inversa de una Cola


### Descripción del Programa

Este programa implementa una solución recursiva en Python para invertir el orden de una cola sin eliminar ningún elemento. Utilizando la estructura `deque` del módulo `collections`, la función `invertirCola` vacía la cola de forma recursiva y luego reinserta cada elemento al final, logrando así invertir el orden original.

## Funcionamiento del Programa

El flujo del programa es el siguiente:

1. Se inicializa una cola y se llena con una secuencia de números (en este caso, los números 1 a 6 repetidos cinco veces).
2. Se muestra la cola original.
3. Se llama a la función `invertirCola` para invertir la cola.
4. Se muestra la cola invertida.

## Código Fuente

```python
from collections import deque


def invertirCola(cola: deque):
    # Caso base: si la cola está vacía, se detiene la recursión.
    if not cola:
        return

    frente = cola.popleft()

    # Llamada recursiva para invertir el resto de la cola.
    invertirCola(cola)

    # Reinserta el elemento al final de la cola.
    cola.append(frente)


def main():
    # Inicializamos la cola.
    cola = deque()

    # Agregamos los elementos 1 a 6 repetidos 5 veces.
    for num in [1, 2, 3, 4, 5, 6] * 5:
        cola.append(num)

    print("Cola original:", list(cola))

    # Invertimos la cola.
    invertirCola(cola)

    print("Cola invertida:", list(cola))


if __name__ == '__main__':
    main()

```

#--------------------------------------------------------------------------

# Determinar el Inverso de una Cola


### Descripción del Programa

Este programa implementa dos funcionalidades clave:

1. **Función 1:** Verifica si una cola (`C1`) es el inverso de una pila (`P1`).  
   Para ello, se copian ambas estructuras en variables temporales. La función extrae elementos de la pila (utilizando `pop()`) y de la cola (utilizando `popleft()`), comparándolos para confirmar si la cola representa la inversión exacta de la pila.

2. **Función 2:** Crea una nueva cola (`C1`) que contiene los elementos de la pila (`P1`) que no se encuentran en otra pila (`P2`).  
   La función recorre todos los elementos de `P1` y, para cada uno, verifica si está presente en `P2`. Si no lo está, se añade a la cola `C1`.

### Funcionamiento del Programa

El programa sigue los siguientes pasos:

1. Se definen dos pilas y una cola:
   - **P1:** Pila con los números 10, 20, 30, 40, 50 y 60.
   - **C1:** Cola con los mismos números que P1 pero en orden inverso (60, 50, 40, 30, 20, 10).
   - **P2:** Otra pila con algunos de los elementos de P1 y un elemento adicional (80).

2. Se muestran los contenidos iniciales de las estructuras.

3. Se ejecuta la **Función 1** para verificar si la cola `C1` es el inverso de la pila `P1`, mostrando el resultado de la verificación.

4. Se ejecuta la **Función 2** para generar una nueva cola que contiene los elementos de `P1` que no están presentes en `P2`, mostrando el resultado final.

### Código Fuente

```python
from collections import deque

def funcion1(P1, C1):
    if len(P1) != len(C1):
        return False
    
    tempStack = list(P1)
    tempQueue = deque(C1)
    
    while tempStack:
        if tempStack.pop() != tempQueue.popleft():
            return False
    return True

def funcion2(P1, P2):
    C1 = deque()
    for elementoP1 in P1:
        encontrado = False
        for elementoP2 in P2:
            if elementoP1 == elementoP2:
                encontrado = True
                break
        if not encontrado:
            C1.append(elementoP1)
    return C1

def mostrarPila(pila):
    print("Pila:", pila)

def mostrarCola(cola):
    print("Cola:", list(cola))

def main():
    P1 = []
    P1.append(10)
    P1.append(20)
    P1.append(30)
    P1.append(40)
    P1.append(50)
    P1.append(60)
    
    C1 = deque()
    C1.append(60)
    C1.append(50)
    C1.append(40)
    C1.append(30)
    C1.append(20)
    C1.append(10)
    
    P2 = []
    P2.append(20)
    P2.append(40)
    P2.append(60)
    P2.append(80)
    
    print("Contenido inicial de las estructuras:")
    mostrarPila(P1)
    mostrarCola(C1)
    mostrarPila(P2)
    
    print("\n¿C1 es el inverso de P1?", funcion1(P1, C1))
    
    resultado = funcion2(P1, P2)
    print("\nElementos de P1 que no están en P2:")
    mostrarCola(resultado)

if __name__ == '__main__':
    main()
```

# ---------------------------------------------------------------

# Eliminar los Repetidos

### Descripción del Programa

Este programa en Python elimina todas las ocurrencias de un número específico de una **cola**, y las coloca en una **cola auxiliar**. Los elementos que no coinciden con el número a eliminar se mantienen en la **cola original**. Al final, el programa imprime la **cola original** después de la eliminación, los **elementos eliminados** en la **cola auxiliar** y el **número total de eliminaciones**.

### Funcionamiento del Programa

1. **Generación de la Cola Original:**
   Se genera una cola con **30 elementos aleatorios** entre 0 y 9, con algunos números repetidos.

2. **Selección del Número a Eliminar:**
   El programa selecciona un número aleatorio (entre 0 y 9) que se eliminará de la cola original.

3. **Eliminación de Ocurrencias:**
   El programa recorre la cola y elimina todas las ocurrencias del número seleccionado. Estos elementos eliminados se agregan a una cola auxiliar.

4. **Resultados:**
   Al final, el programa imprime:
   - La **cola original** con los elementos restantes después de eliminar el número.
   - La **cola auxiliar** con los elementos eliminados.
   - El **número total de eliminaciones**.

### Código Fuente

```python
import random
from collections import deque

def eliminar_repetidos(cola, dato):
    # Cola auxiliar para almacenar los elementos eliminados
    cola_aux = deque()

    # Iteramos sobre los elementos de la cola original
    # Y eliminamos las ocurrencias del dato especificado
    contador = 0
    size = len(cola)

    for _ in range(size):
        elemento = cola.popleft()  # Sacamos el primer elemento de la cola

        if elemento == dato:
            cola_aux.append(elemento)  # Si es igual al dato, lo añadimos a la cola auxiliar
            contador += 1
        else:
            cola.append(elemento)  # Si no es igual al dato, lo devolvemos a la cola original

    # Imprimir el resultado
    print("Cola después de eliminar", dato, ":", list(cola))
    print("Elementos extraídos (cola):", list(cola_aux))
    print("Número total de elementos extraídos:", contador)

def main():
    # Crear una cola original re
