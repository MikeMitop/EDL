import random

class Producto:
    def __init__(self, codigo, cantidad, precio, count=1):
        self.codigo = codigo
        self.cantidad = cantidad
        self.precio = precio
        self.count = count

    def __str__(self):
        return f"Código: {self.codigo:4d} | Cantidad: {self.cantidad:3d} | Precio: {self.precio:6.2f}"


def poblar_datos(lista, n):
    for _ in range(n):
        producto = Producto(
            random.randint(1000, 9999),
            random.randint(1, 10),
            round(random.uniform(10, 200), 2)
        )
        lista.append(producto)


def mostrar_datos(lista):
    for producto in lista:
        print(producto)


def suma_ventas(lista_entrada, lista_salida):
    lista_ordenada = sorted(lista_entrada, key=lambda p: p.codigo)

    if not lista_ordenada:
        return

    ultimo_producto = lista_ordenada[0]

    for producto_actual in lista_ordenada[1:]:
        if producto_actual.codigo == ultimo_producto.codigo:
            nuevo_count = ultimo_producto.count + 1
            nuevo_precio = round((ultimo_producto.precio * ultimo_producto.count + producto_actual.precio) / nuevo_count, 2)
            ultimo_producto = Producto(
                ultimo_producto.codigo,
                ultimo_producto.cantidad + producto_actual.cantidad,
                nuevo_precio,
                nuevo_count
            )
        else:
            lista_salida.append(ultimo_producto)
            ultimo_producto = producto_actual

    lista_salida.append(ultimo_producto)


if __name__ == "__main__":
    print("Ejercicio #1 Lista Productos Vendidos Totalizada")
    print("=" * 50)

    ventas = []
    totalizadas = []

    poblar_datos(ventas, 15)

    print("\nDatos de ventas originales:")
    print("-" * 50)
    mostrar_datos(ventas)

    suma_ventas(ventas, totalizadas)

    print("\nDatos de ventas totalizadas por producto:")
    print("-" * 50)
    mostrar_datos(totalizadas)
