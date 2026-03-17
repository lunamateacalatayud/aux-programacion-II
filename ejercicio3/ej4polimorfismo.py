# ejercicio 4
# Luna Mariana Calatayud
class Videojuego:
    def __init__(self, nombre="Desconocido", plataforma="Desconocida", jugadores=1):
        self.__nombre = nombre
        self.__plataforma = plataforma
        self.__jugadores = jugadores

    def agregarJugadores(self, cant=None):
        if cant is None:
            self.__jugadores += 1
        else:
            self.__jugadores += cant

    def mostrar(self):
        print("Nombre:", self.__nombre)
        print("Plataforma:", self.__plataforma)
        print("Jugadores:", self.__jugadores)
        print()

juego1 = Videojuego("FIFA", "PlayStation")
juego2 = Videojuego("Minecraft", jugadores=2)

juego1.agregarJugadores()

cant = int(input("cantidad de jugadores a agregar: "))
juego2.agregarJugadores(cant)

juego1.mostrar()
juego2.mostrar()
