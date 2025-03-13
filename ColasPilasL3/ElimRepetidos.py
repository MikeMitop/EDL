import random
from collections import deque
def eliminar_repetidos(pila, cola, dato, contador):
    # Caso base: si la pila está vacía, imprimir resultados y retornar el contador
    if not pila:
        print("Elementos extraídos (cola):", list(cola))
        print("Número total de elementos extraídos:", contador)
        print("Pila después del proceso:", pila)
        return contador

    # Extraer el elemento superior de la pila
    elemento = pila.pop()

    if elemento == dato:
        # Si el elemento es igual al dato, se agrega a la cola y se incrementa el contador
        cola.append(elemento)
        contador += 1
    else:
        # Si el elemento no es igual, se llama recursivamente sin modificar la pila
        contador = eliminar_repetidos(pila, cola, dato, contador)
        # Se restaura el elemento no extraído a la pila
        pila.append(elemento)
        return contador

    # Llamada recursiva para procesar el resto de la pila
    contador = eliminar_repetidos(pila, cola, dato, contador)
    return contador


def main():
    # Crear una pila representada como lista y una cola usando deque
    pila = []
    cola = deque()

    # Llenar la pila con 10 números aleatorios entre 0 y 9
    for _ in range(10):
        pila.append(random.randint(0, 9))

    print("Pila original:", pila)

    # Seleccionar un número aleatorio a eliminar
    dato = random.randint(0, 9)
    print("Número a eliminar:", dato)

    # Ejecutar la función de eliminación
    eliminar_repetidos(pila, cola, dato, 0)


if __name__ == '__main__':
    main()
