# Primer Parcial: Colas

## Objetivos 

* Desarollar el pensamiento lógico y algorítmico.
* Aplicar estructuras dinámicas como lo son las colas ('FIFO') para resolver problemas.
* Implementar operaciones de colas tales como 'enqueue' o 'dequeue'
* Comprender las diferencias y aplicaciones prácticas de las estructuras de datos lineales.
* Fortalecimiento de las habilidades al momento de implementar un código basandose en un algoritmo.

## Descripción del algoritmo/problema

El simulador se encarga de gestionar una zona de parqueo con comportamiento de FIFO (First in, First out), basandose en:

### 1. Ingreso de los Vehículos

Los vehículos, llegan por el extremo sur de la vía y se agregan al final de la cola principal si hay espacio disponbile.

### 2. Retiro de Vehículos por su número de placa

El funcionario puede retirar un vehículo dependiendo de su placa. Y se realiza el proceso del retiro del auto teniendo en cuenta de:

### 2.1 Auto en el Extremo norte:

- Se retira directamente desde el inicio de la vía.

### 2.2 Auto en otro lugar:

- Se mueven los autos uno por uno, hasta que se encuentre el coche que desea salir.
- Los autos desplazados se vuelven a ingresar por el extremo sur, esto a modo de conservar el orden de llegada de los autos.

- # ¿Cumple con los Requerimientos de la implementación?

| Requisito del enunciado                                 | ¿Está implementado? |
|---------------------------------------------------------|----------------------|
| Llegada por el extremo sur                              |  Sí                 |
| Salida por el extremo norte                             |  Sí                 |
| Selección de auto por placa                             |  Sí                 |
| Reorganización de autos si no está en el norte          |  Sí                 |
| Mantenimiento del orden de llegada                      |  Sí                 |
| Control de espacio disponible                           |  Sí                 |
| Cola de espera si la vía está llena                     |  Sí                 |
| Paso automático de espera a vía al liberar espacio      |  Sí                 |
| Conteo de movimientos del auto                          |  Sí                 |
| Conteo de autos movidos para retiro                     |  Sí                 |
| Visualización del estado actual del parqueo             |  Sí                 |

# Código Fuente

``` python
from collections import deque
class Auto:
    def __init__(self, placa): 
        self.placa = placa
        self.movs = 0 
    def mover(self):
        self.movs += 1
    def ver_placa(self):
        return self.placa
    def ver_movs(self):
        return self.movs

class ZonaParqueo:
    def __init__(self, capacidad):
        self.cap = capacidad
        self.via = deque()    
        self.espera = deque()  

    def llegada_auto(self, placa):
        nuevo = Auto(placa)
        if len(self.via) < self.cap:
            self.via.append(nuevo)
            print(f" Auto {placa} entró a la vía.")
        else:
            self.espera.append(nuevo)
            print(f" Vía llena. Auto {placa} en lista de espera.")

    def salida_auto(self, placa):
        if not self.via:
            print("No hay autos en la vía.")
            return

        autos_movidos = 0
        encontrado = False
        total_autos = len(self.via)

        for _ in range(total_autos):
            auto = self.via.popleft()

            if auto.ver_placa() == placa:
                auto.mover()  
                print(f" Auto {placa} salió con {auto.ver_movs()} movimientos.")
                print(f"  (Movimos {autos_movidos} autos para sacarlo)")
                encontrado = True
                break
            else:
                auto.mover()
                print(f"Moviendo {auto.ver_placa()} al final de la vía...")
                self.via.append(auto)
                autos_movidos += 1

        if not encontrado:
            print(f"No se encontró el auto {placa} en la vía.")

        if self.espera:
            siguiente = self.espera.popleft()
            self.via.append(siguiente)
            print(f" Auto {siguiente.ver_placa()} pasó de la lista de espera a la vía.")


    def mostrar_estado(self):
        print("\n=== ESTADO DEL PARQUEO ===")
        print("Vía:")
        if not self.via:
            print("  [Vía vacía]")
        else:
            for i, auto in enumerate(self.via):
                print(f"  {i+1}) {auto.ver_placa()} - Movs: {auto.ver_movs()}")
        print("\nEspera:")
        if not self.espera:
            print("  [No hay autos en espera]")
        else:
            for i, auto in enumerate(self.espera):
                print(f"  {i+1}) {auto.ver_placa()}")
        print("===========================\n")

   
if __name__ == "__main__":
    parqueo = ZonaParqueo(8)
    parqueo.llegada_auto("ABC123")
    parqueo.llegada_auto("DEF456")
    parqueo.llegada_auto("GHI789")
    parqueo.llegada_auto("JKL012")
    parqueo.llegada_auto("MNO345")
    parqueo.llegada_auto("PQR678") 
    parqueo.llegada_auto("STU901")
    parqueo.llegada_auto("VWX234")
    parqueo.llegada_auto("YZA567")
    parqueo.llegada_auto("BCD890")
    parqueo.llegada_auto("EFG123")
    parqueo.mostrar_estado()
    parqueo.salida_auto("DEF456")
    parqueo.salida_auto("ABC123")
    parqueo.mostrar_estado()

```



## Estructura del Código

### Clase Auto: 

* Se encarga de guardar los siguientes datos:
       * La o las Placas del Auto.
       * El numero de veces que se mueve el auto dentro de la vía.
  
* **Los métodos que se usaron dentro de la clase Auto son:**
  * mover(), para incrementar en el contador de movimientos del auto. Se invoca cada vez que el auto se mueve dentro de la vía.
  * ver_placa(), Retorna el número de placa del auto, el método se utiliza para identificar los autos al ser buscados.
  * ver_movs(), Devuelve el número total de movimientos del auto, se muestra cuando el auto se retira de la vía.
  
  
### Clase ZonaParqueo:

* Tiene como atributos:
      - cap: Significa la capacidad  máxima  de la vía
      - via : Significa la cola de autos en la vía
      - espera: Significa la cola de autos en espera
* **Los métodos que se usaron en la clase ZonaParqueo son:**
    
  - llegada_auto(placa), Recibe un auto nuevo por el extremo sur. Si hay espacio, se agrega al final de la vía. Si la vía está llena, se agrega a la cola de espera.
  - salida_auto(placa),  Permite retirar un auto específico por su placa. Si el auto no está al inicio de la vía (extremo norte), se reubican los autos hacia el final hasta encontrarlo.
  - mostrar_estado(), Muestra el estado actual del sistema de parqueo.

# Explicación del Código

 
El programa está estructurado en dos clases principales (`Auto` y `ZonaParqueo`) y una sección principal de ejecución (`main`).

###  Clase `Auto`
- Representa cada automóvil que ingresa al parqueadero.
- Guarda la **placa** del auto y la **cantidad de movimientos internos** que ha tenido dentro de la vía.
- Incluye métodos para:
  - Aumentar los movimientos (`mover()`),
  - Consultar la placa (`ver_placa()`),
  - Consultar el número de movimientos (`ver_movs()`).

###  Clase `ZonaParqueo`
- Controla el comportamiento de la zona de parqueo.
- Contiene:
  - Una **cola principal `via`**, que representa los autos parqueados (vía de acceso).
  - Una **cola secundaria `espera`**, para autos que no pudieron ingresar por falta de espacio.

- Métodos clave:
  - `llegada_auto(placa)`: Ingresa el auto por el extremo sur. Si la vía está llena, se guarda en espera.
  - `salida_auto(placa)`: Busca el auto por su placa. Si no está al frente, se reubican los demás autos hasta que el auto buscado esté al inicio. Se registra cuántas veces se movieron los autos.
  - `mostrar_estado()`: Muestra la situación actual de la vía y la cola de espera, incluyendo los movimientos de cada auto.

###  Flujo general del programa (main)
- Se inicializa un parqueadero con una capacidad máxima.
- Se insertan varios autos, algunos quedan en espera por falta de espacio.
- Luego se retiran autos específicos por su placa.
- Se muestran los movimientos de cada auto al salir y el total de autos que se movieron para sacarlo.
- También se actualiza la vía automáticamente pasando autos desde la lista de espera cuando haya espacio disponible.

