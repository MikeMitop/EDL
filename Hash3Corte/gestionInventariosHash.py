import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class Producto:
    
    def __init__(self, sku, nombre, descripcion, cantidad):
        
        self.sku = sku
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
    
    def __str__(self):
        
        return f"SKU: {self.sku}, Nombre: {self.nombre}, Cantidad: {self.cantidad}"


class TablaHashInventario:
   
    
    def __init__(self, tamanio=211):
        
        self.tamanio = tamanio
        self.tabla = [[] for _ in range(tamanio)]
    
    def hash_cadena(self, clave):
        
        h = 0
        for c in clave:
            h = (h * 31 + ord(c)) % self.tamanio
        return h
    
    def agregar_producto(self, producto):
        
        indice = self.hash_cadena(producto.sku)
        
        for prod in self.tabla[indice]:
            if prod.sku == producto.sku:
                return False  
        self.tabla[indice].append(producto)
        return True
    
    def buscar_producto(self, sku):
        
        indice = self.hash_cadena(sku)
        
        
        for producto in self.tabla[indice]:
            if producto.sku == sku:
                return producto
        
        return None
    
    def actualizar_cantidad(self, sku, nueva_cantidad):
        
        producto = self.buscar_producto(sku)
        
        if producto is None:
            return False
        
        producto.cantidad = nueva_cantidad
        return True
    
    def eliminar_producto(self, sku):
        
        indice = self.hash_cadena(sku)
        
        for i, producto in enumerate(self.tabla[indice]):
            if producto.sku == sku:
                self.tabla[indice].pop(i)
                return True
        
        return False 
    def obtener_todos_productos(self):
      
        todos_productos = []
        for i in range(self.tamanio):
            todos_productos.extend(self.tabla[i])
        return todos_productos
    
    def mostrar_inventario(self):
        
        print("\n=== INVENTARIO ACTUAL ===")
        productos_totales = 0
        
        for i, bucket in enumerate(self.tabla):
            if bucket:  
                print(f"\nBucket {i}:")
                for producto in bucket:
                    print(f"  {producto}")
                    productos_totales += 1
        
        print(f"\nTotal de productos: {productos_totales}")


def ejecutar_interfaz_grafica():
    
    root = tk.Tk()
    root.title("Sistema de Inventario - Tabla Hash")
    root.geometry("800x600")
    
 
    inventario = TablaHashInventario(tamanio=10)  
    
   
    productos_ejemplo = [
        Producto("E001", "iPhone de Santi Arruru", "Teléfono inteligente de última generación", 15),
        Producto("E002", "CUenta de Netflix", "Servicio de Streaming", 8),
        Producto("E003", "Cafe", "Cafe del caqueta", 20),
        Producto("E004", "Tablet de Santi Arruru", "Tablet De Santi", 12),
        Producto("E005", "PC de Santi Arruru", "PC De Santi", 5)
    ]
    
    for producto in productos_ejemplo:
        inventario.agregar_producto(producto)
    
    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)
    
    tab_agregar = ttk.Frame(notebook)
    tab_buscar = ttk.Frame(notebook)
    tab_actualizar = ttk.Frame(notebook)
    tab_eliminar = ttk.Frame(notebook)
    tab_listar = ttk.Frame(notebook)
    
    notebook.add(tab_agregar, text="Agregar Producto")
    notebook.add(tab_buscar, text="Buscar Producto")
    notebook.add(tab_actualizar, text="Actualizar Cantidad")
    notebook.add(tab_eliminar, text="Eliminar Producto")
    notebook.add(tab_listar, text="Listar Productos")
    
    entry_sku_agregar = ttk.Entry(tab_agregar, width=30)
    entry_nombre = ttk.Entry(tab_agregar, width=30)
    entry_descripcion = ttk.Entry(tab_agregar, width=30)
    entry_cantidad = ttk.Entry(tab_agregar, width=30)
    
    entry_sku_buscar = ttk.Entry(tab_buscar, width=30)
    text_resultado_buscar = scrolledtext.ScrolledText(tab_buscar, width=50, height=10)
    
    entry_sku_actualizar = ttk.Entry(tab_actualizar, width=30)
    entry_nueva_cantidad = ttk.Entry(tab_actualizar, width=30)
    
    entry_sku_eliminar = ttk.Entry(tab_eliminar, width=30)
    
    columns = ("SKU", "Nombre", "Descripción", "Cantidad")
    tree = ttk.Treeview(tab_listar, columns=columns, show="headings")
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)
    
    tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    
    scrollbar = ttk.Scrollbar(tab_listar, orient="vertical", command=tree.yview)
    scrollbar.grid(row=1, column=1, sticky="ns")
    tree.configure(yscrollcommand=scrollbar.set)
    
    tab_listar.grid_rowconfigure(1, weight=1)
    tab_listar.grid_columnconfigure(0, weight=1)
    
    def listar_productos():
        for item in tree.get_children():
            tree.delete(item)
        
        productos = inventario.obtener_todos_productos()
        
        for producto in productos:
            tree.insert("", "end", values=(producto.sku, producto.nombre, producto.descripcion, producto.cantidad))
    
    def agregar_producto():
        sku = entry_sku_agregar.get().strip()
        nombre = entry_nombre.get().strip()
        descripcion = entry_descripcion.get().strip()
        
        if not sku or not nombre or not descripcion:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        try:
            cantidad = int(entry_cantidad.get().strip())
            if cantidad < 0:
                messagebox.showerror("Error", "La cantidad debe ser un número positivo")
                return
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero")
            return
        
        producto = Producto(sku, nombre, descripcion, cantidad)
        if inventario.agregar_producto(producto):
            messagebox.showinfo("Éxito", f"Producto con SKU {sku} agregado correctamente")
            entry_sku_agregar.delete(0, tk.END)
            entry_nombre.delete(0, tk.END)
            entry_descripcion.delete(0, tk.END)
            entry_cantidad.delete(0, tk.END)
            listar_productos()
        else:
            messagebox.showerror("Error", f"Ya existe un producto con el SKU {sku}")
    
    def buscar_producto():
        sku = entry_sku_buscar.get().strip()
        
        if not sku:
            messagebox.showerror("Error", "El SKU es obligatorio")
            return
        
        producto = inventario.buscar_producto(sku)
        
        text_resultado_buscar.delete(1.0, tk.END)
        if producto:
            text_resultado_buscar.insert(tk.END, f"SKU: {producto.sku}\n")
            text_resultado_buscar.insert(tk.END, f"Nombre: {producto.nombre}\n")
            text_resultado_buscar.insert(tk.END, f"Descripción: {producto.descripcion}\n")
            text_resultado_buscar.insert(tk.END, f"Cantidad: {producto.cantidad}\n")
        else:
            text_resultado_buscar.insert(tk.END, f"No se encontró un producto con el SKU: {sku}")
    
    def actualizar_cantidad():
        sku = entry_sku_actualizar.get().strip()
        
        if not sku:
            messagebox.showerror("Error", "El SKU es obligatorio")
            return
        
        try:
            nueva_cantidad = int(entry_nueva_cantidad.get().strip())
            if nueva_cantidad < 0:
                messagebox.showerror("Error", "La cantidad debe ser un número positivo")
                return
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero")
            return
        
        if inventario.actualizar_cantidad(sku, nueva_cantidad):
            messagebox.showinfo("Éxito", f"Cantidad del producto con SKU {sku} actualizada correctamente")
            entry_sku_actualizar.delete(0, tk.END)
            entry_nueva_cantidad.delete(0, tk.END)
            listar_productos()
        else:
            messagebox.showerror("Error", f"No existe un producto con el SKU {sku}")
    
    def eliminar_producto():
        sku = entry_sku_eliminar.get().strip()
        
        if not sku:
            messagebox.showerror("Error", "El SKU es obligatorio")
            return
        
        if inventario.eliminar_producto(sku):
            messagebox.showinfo("Éxito", f"Producto con SKU {sku} eliminado correctamente")
            entry_sku_eliminar.delete(0, tk.END)
            listar_productos()
        else:
            messagebox.showerror("Error", f"No existe un producto con el SKU {sku}")
    
    ttk.Label(tab_agregar, text="SKU:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_sku_agregar.grid(row=0, column=1, padx=10, pady=10)
    
    ttk.Label(tab_agregar, text="Nombre:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_nombre.grid(row=1, column=1, padx=10, pady=10)
    
    ttk.Label(tab_agregar, text="Descripción:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    entry_descripcion.grid(row=2, column=1, padx=10, pady=10)
    
    ttk.Label(tab_agregar, text="Cantidad:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
    entry_cantidad.grid(row=3, column=1, padx=10, pady=10)
    
    ttk.Button(tab_agregar, text="Agregar Producto", command=agregar_producto).grid(row=4, column=0, columnspan=2, pady=20)
    
    ttk.Label(tab_buscar, text="SKU:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_sku_buscar.grid(row=0, column=1, padx=10, pady=10)
    
    ttk.Button(tab_buscar, text="Buscar Producto", command=buscar_producto).grid(row=1, column=0, columnspan=2, pady=20)
    
    ttk.Label(tab_buscar, text="Resultado:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    text_resultado_buscar.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    
    ttk.Label(tab_actualizar, text="SKU:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_sku_actualizar.grid(row=0, column=1, padx=10, pady=10)
    
    ttk.Label(tab_actualizar, text="Nueva Cantidad:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_nueva_cantidad.grid(row=1, column=1, padx=10, pady=10)
    
    ttk.Button(tab_actualizar, text="Actualizar Cantidad", command=actualizar_cantidad).grid(row=2, column=0, columnspan=2, pady=20)
    
    ttk.Label(tab_eliminar, text="SKU:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_sku_eliminar.grid(row=0, column=1, padx=10, pady=10)
    
    ttk.Button(tab_eliminar, text="Eliminar Producto", command=eliminar_producto).grid(row=1, column=0, columnspan=2, pady=20)
    
    ttk.Button(tab_listar, text="Actualizar Lista", command=listar_productos).grid(row=0, column=0, pady=10)
    
    listar_productos()
    
    root.mainloop()


def ejecutar_pruebas_consola():
    
    inventario = TablaHashInventario(tamanio=10)
    
    productos = [
        Producto("E001", "iPhone de Santi Arruru", "Teléfono de Marca Apple", 15),
        Producto("E002", "CUenta de Netflix", "Servicio de Streaming", 8),
        Producto("E003", "Cafe", "Cafe del caqueta", 20),
        Producto("E004", "Tablet de Santi Arruru", "Tablet de Marca Samsung", 12),
        Producto("E005", "Monitor de Santi Arruru", "Monitor curvo de 34 pulgadas", 5)
    ]
    
    print("Agregando productos al inventario...")
    for producto in productos:
        if inventario.agregar_producto(producto):
            print(f"Agregado: {producto}")
        else:
            print(f"Error: No se pudo agregar el producto {producto.sku}")
    
    inventario.mostrar_inventario()
    
    print("\n=== BÚSQUEDA DE PRODUCTOS ===")
    sku_existente = "E003"
    sku_no_existente = "E999"
    
    producto_encontrado = inventario.buscar_producto(sku_existente)
    if producto_encontrado:
        print(f"Producto encontrado: {producto_encontrado}")
    else:
        print(f"No se encontró un producto con SKU: {sku_existente}")
    
    producto_no_encontrado = inventario.buscar_producto(sku_no_existente)
    if producto_no_encontrado:
        print(f"Producto encontrado: {producto_no_encontrado}")
    else:
        print(f"No se encontró un producto con SKU: {sku_no_existente}")
    
    print("\n=== ACTUALIZACIÓN DE CANTIDAD ===")
    sku_actualizar = "E001"
    nueva_cantidad = 25
    
    if inventario.actualizar_cantidad(sku_actualizar, nueva_cantidad):
        print(f"Cantidad del producto {sku_actualizar} actualizada a {nueva_cantidad}")
        producto_actualizado = inventario.buscar_producto(sku_actualizar)
        print(f"Producto actualizado: {producto_actualizado}")
    else:
        print(f"Error: No existe un producto con el SKU {sku_actualizar}")
    
    if not inventario.actualizar_cantidad(sku_no_existente, 10):
        print(f"Error (esperado): No existe un producto con el SKU {sku_no_existente}")
    
    print("\n=== ELIMINACIÓN DE PRODUCTO ===")
    sku_eliminar = "E004"
    
    print("Inventario antes de eliminar:")
    inventario.mostrar_inventario()
    
    if inventario.eliminar_producto(sku_eliminar):
        print(f"Producto con SKU {sku_eliminar} eliminado correctamente")
    else:
        print(f"Error: No existe un producto con el SKU {sku_eliminar}")
    
    print("\nInventario después de eliminar:")
    inventario.mostrar_inventario()
    
    print("\n=== PRUEBA DE SKU DUPLICADO ===")
    producto_duplicado = Producto(sku_existente, "Producto Duplicado", "Este SKU ya existe", 5)
    if not inventario.agregar_producto(producto_duplicado):
        print(f"Error (esperado): Ya existe un producto con el SKU {sku_existente}")
    
    print("\nPruebas completadas.")


if __name__ == "__main__":
    try:
        ejecutar_interfaz_grafica()
    except Exception as e:
        print(f"No se pudo iniciar la interfaz gráfica: {e}")
        print("Ejecutando pruebas en consola...")
        ejecutar_pruebas_consola()
