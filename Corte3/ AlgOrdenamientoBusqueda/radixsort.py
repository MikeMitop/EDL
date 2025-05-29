def countingSort(arr, exp, base):
    n = len(arr)
    output = [0] * n  # Lista  para almacenar el resultado ordenado
    cubetas = [0] * base  # Punto 2: Creamos las cubetas (base=16 para hexadecimal)
    
    # Punto 4: Se coloca cada elemento en su cubeta correspondiente según el dígito actual
    for i in range(n):
        index = arr[i] // exp
        cubetas[index % base] += 1
    
    # Se calculan las posiciones finales  para cada cubeta
    for i in range(1, base):
        cubetas[i] += cubetas[i - 1]
    
    # Punto 5: Se recompilan los elementos de las cubetas en la lista  (output)
    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        pos = index % base
        cubetas[pos] -= 1
        output[cubetas[pos]] = arr[i]
    
    # Copiamos los elementos ordenados de vuelta al arreglo original
    for i in range(n):
        arr[i] = output[i]

def radixSort(arr, base):
    # Punto 1:  longitud máxima implícitamente al encontrar el valor máximo
    max1 = max(arr)
    exp = 1
    
    # Punto 3: Se itera sobre cada dígito, comenzando por el menos significativo (exp=1)
    # Punto 6: Repetir el proceso para cada dígito (counting sort)
    while max1 // exp > 0:
        countingSort(arr, exp, base)
        exp *= base
    
    # Punto 7:  El arreglo arr contiene las claves ordenadas

# Conversion de  los números hexadecimales a decimales 
numeros_hex = ["1C8", "A89", "401", "16C", "1E2", "173"]

numeros_decimal = []
for hex_num in numeros_hex:
    decimal = int(hex_num, 16)
    numeros_decimal.append(decimal)

print("Números originales en decimal:", numeros_decimal)

# Algoritmo Radix Sort con base 16 (para hexadecimales)
radixSort(numeros_decimal, 16)

print("Números ordenados en decimal:", numeros_decimal)

# Convertimos de vuelta a hexadecimal para mostrar el resultado
numeros_hex_ordenados = []
for num in numeros_decimal:
    hex_num = format(num, 'X')
    numeros_hex_ordenados.append(hex_num)

print("Números ordenados en hexadecimal:", numeros_hex_ordenados)
