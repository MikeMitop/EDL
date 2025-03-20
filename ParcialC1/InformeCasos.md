# Desglose de los casos y su respectiva explicación de funcionamiento.

##  Los automóviles llegan por el extremo sur de la vía y salen por el extremo norte de la misma.

En el programa, se utiliza una estructura `deque` ( cola doble) para representar la vía. Esto permite controlar ambos extremos fácilmente.

El método append() agrega el auto al final de la vía, simulando el ingreso por el extremo sur.

append() significa: añadir un elemento al final de una estructura.


self. -  permite acceder a los atributos y métodos del mismo objeto desde dentro de su clase.



*El método popleft() elimina el primer auto que ingresó, el que está más cerca del extremo norte.

 *  popleft() significa: sacar el primer elemento de la cola (el que lleva más tiempo).

----
----
---
---


# 📄 InformeCasos.md - Simulador Zona de Parqueo Pago

Este documento tiene como objetivo demostrar que el simulador implementado **cumple plenamente con todos los casos funcionales y condiciones requeridas** en el enunciado de la evaluación de la asignatura **Estructuras de Datos Lineales**, correspondiente a las zonas de parqueo pago en vía autorizadas por la Alcaldía Mayor de Bogotá.

---

## ✅ Tabla de cumplimiento por requisito

| Requisito del enunciado                                | ¿Está implementado? |
|--------------------------------------------------------|----------------------|
| Llegada por el extremo sur                             | Sí                   |
| Salida por el extremo norte                            | Sí                   |
| Selección de auto por placa                            | Sí                   |
| Reorganización de autos si no está en el norte         | Sí                   |
| Mantenimiento del orden de llegada                     | Sí                   |
| Control de espacio disponible                          | Sí                   |
| Cola de espera si la vía está llena                    | Sí                   |
| Paso automático de espera a vía al liberar espacio     | Sí                   |
| Conteo de movimientos del auto                         | Sí                   |
| Conteo de autos movidos para retiro                    | Sí                   |
| Visualización del estado actual del parqueo            | Sí                   |

---

## 📘 Justificación detallada por caso

### ✔ Caso A - **Ingreso y salida en orientación Sur-Norte**

> "Los automóviles llegan por el extremo sur de la vía y salen por el extremo norte de la misma."

- **¿Dónde se ve en el código?**
  - En `llegada_auto()`: `self.via.append(nuevo)` simula entrada por el sur.
  - En `salida_auto()`: `self.via.popleft()` simula salida por el norte.

- **¿Cómo funciona?**
  - **`append()`** es un método propio de las estructuras tipo `deque` (cola doble), que agrega elementos **al final** de la estructura. En este caso, representa el **extremo sur** de la vía.
  - **`popleft()`** remueve el primer elemento de la cola, que representa el **extremo norte**.

- **¿Qué significa `self`?**
  - `self` en Python hace referencia al **objeto actual** de la clase. En este contexto, `self.via` se refiere a la **vía** del parqueo del objeto `ZonaParqueo` que está en ejecución. Permite acceder a los atributos internos del objeto desde sus propios métodos.

---

### ✔ Caso B - **Selección de auto por número de placa**

> "El funcionario selecciona el automóvil por el número de la placa."

- **¿Dónde se ve en el código?**
  - En `salida_auto(placa)` se recorre la vía y se compara: `if auto.ver_placa() == placa:`.

- **¿Cómo funciona?**
  - Se puede identificar cualquier auto específico en la vía utilizando su placa. El método `ver_placa()` devuelve el número de placa para comparación.

---

### ✔ Caso 1 - **Auto en el extremo norte**

> "Si el automóvil se encuentra parqueado en el extremo norte, se procede a sacarlo directamente."

- **¿Dónde se ve en el código?**
  - El primer auto extraído del `popleft()` (el inicio de la `deque`) se compara. Si coincide con la placa deseada, se retira sin necesidad de mover otros autos.

- **¿Cómo se identifica este caso?**
  - Si el auto buscado es el primero en el recorrido, se cumple directamente el caso 1.

---

### ✔ Caso 2 - **Auto no en el extremo norte**

> "Si no está en el extremo norte, se mueven los automóviles hasta ubicarlo, y se reinsertan al final conservando el orden."

- **¿Dónde se ve en el código?**
  - En el bucle de `salida_auto()`, los autos que no son el buscado se mueven al final mediante `self.via.append(auto)`.

- **¿Cómo funciona esto?**
  - Mientras se recorre la vía, los autos que no son el buscado son extraídos (con `popleft()`) y **reinsertados al final con `append()`**.
  - De este modo, **se respeta el orden original** y el auto deseado puede llegar al frente para ser retirado.

---

### ✔ Control del espacio disponible y cola de espera

> "Si no hay espacio, el nuevo automóvil pasa a la cola de espera."

- **¿Dónde se ve en el código?**
  - En `llegada_auto()` cuando `len(self.via) >= self.cap`, se ejecuta `self.espera.append(nuevo)`.

- **¿Cómo funciona?**
  - Si el tamaño actual de la vía ha alcanzado su capacidad máxima, el auto se añade a la lista de espera utilizando nuevamente `append()`.

---

### ✔ Paso automático desde la cola de espera

> "Cuando queda espacio, debe pasar automáticamente un auto de la espera."

- **¿Dónde se ve en el código?**
  - Al final de `salida_auto()`:
    ```python
    if self.espera:
        siguiente = self.espera.popleft()
        self.via.append(siguiente)
    ```

- **¿Cómo funciona?**
  - Cuando un auto sale, se revisa si hay autos en espera. Si los hay, se **retira el primero de la cola (`popleft()`)** y se inserta en la vía con `append()`.

---

### ✔ Conteo de movimientos del auto

> "Debe mostrarse cuántas veces se movió el auto dentro de la vía."

- **¿Dónde se ve en el código?**
  - En la clase `Auto`, método `mover()` incrementa un contador.
  - Se invoca cada vez que el auto es movido por reubicación o salida.

- **¿Dónde se muestra?**
  - En `salida_auto()`, al encontrar el auto deseado:
    ```python
    print(f" Auto {placa} salió con {auto.ver_movs()} movimientos.")
    ```

---

### ✔ Conteo de autos movidos para sacar uno

> "Mostrar cuántos autos fueron movidos para sacar el deseado."

- **¿Dónde se ve en el código?**
  - La variable `autos_movidos` se incrementa dentro del bucle cada vez que se mueve un auto diferente al buscado.

- **¿Dónde se muestra?**
  ```python
  print(f"  (Movimos {autos_movidos} autos para sacarlo)")
