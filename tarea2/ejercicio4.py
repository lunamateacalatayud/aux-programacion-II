# Ejercicio 4
# Luna Mariana Calatayud
class Bus:
    def __init__(self, capacidad):
        self.__capacidad = capacidad
        self.__pasajeros = 0
        self.__precioPasaje = 1.50
        
    def getCapacidad(self):
        return self.__capacidad
    def getPasajeros(self):
        return self.__pasajeros
    
    def subirPasajeros(self, x):
        if self.__pasajeros + x <= self.__capacidad:
            self.__pasajeros = self.__pasajeros + x
            print("subieron", x, "pasajeros")
        else:
            print("no hay asientos disponibles")

    def cobrarPasaje(self):
        total = self.__pasajeros * self.__precioPasaje
        print("total: Bs.", total)

    def asientosDisponibles(self):
        disp = self.__capacidad - self.__pasajeros
        print("asientos disponibles:", disp)

bus1 = Bus(15)
x = int(input("cantidad de pasajeros: "))
bus1.subirPasajeros(x)
bus1.cobrarPasaje()
bus1.asientosDisponibles()
