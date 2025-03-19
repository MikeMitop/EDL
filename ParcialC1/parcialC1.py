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

#En el bloque de la clase auto, se define la clase Auto con un constructor que recibe la placa del auto. 
# También se define un método mover que incrementa la cantidad de movimientos del auto.
# Además, se definen los métodos ver_placa y ver_movs que devuelven la placa y la cantidad de movimientos del auto, respectivamente.


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

# En el bloque de la clase ZonaParqueo, se define la clase ZonaParqueo con un constructor que recibe la capacidad del parqueo.
# También se define un método llegada_auto que recibe la placa del auto y lo agrega a la vía o a la lista de espera, según corresponda.
# Además, se define el método mostrar_estado que muestra el estado actual del parqueo, incluyendo la cantidad de autos en la vía y en la lista de espera.
 
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

##  En este bloque se define el método salida_auto que recibe la placa del auto que sale del parqueo.
# El método busca el auto en la vía y si lo encuentra, lo elimina de la vía y muestra la cantidad de movimientos que realizó.
# Si el auto no se encuentra en la vía, se mueven los autos que están en la vía al final de la misma hasta encontrar el auto o llegar al final de la vía.
# Si hay autos en la lista de espera, se agrega el siguiente auto a la vía.
 # En el bloque principal del programa, se crea una instancia de la clase ZonaParqueo con una capacidad de 8 autos.
 # Luego se agregan 10 autos a la vía y a la lista de espera.

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

        ## En este bloque se define el método mostrar_estado que muestra el estado actual del parqueo,
        #  incluyendo la cantidad de autos en la vía y en la lista de espera.
        #  También se muestra la cantidad de movimientos que realizó cada auto en la vía.
        #  Si la vía está vacía, se muestra un mensaje indicando que está vacía.
        # Si la lista de espera está vacía, se muestra un mensaje indicando que no hay autos en espera.

   
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
    

## In this main block, we create a ZonaParqueo instance with capacity for 8 cars,
## then add multiple cars (ABC123, DEF456, etc), show the parking state,
## remove two cars (DEF456 and ABC123), and finally show the updated state again
