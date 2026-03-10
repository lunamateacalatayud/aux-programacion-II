# Ejercicio 5
# Luna Mariana Calatayud
class ServidorMinecraft:
    def __init__(self):
        self.__jugadores = []
        self.__diamantes = []
        self.__capacidad = 10

    def agregarJugador(self, nom, diam):
        if len(self.__jugadores) < self.__capacidad:
            self.__jugadores.append(nom)
            self.__diamantes.append(diam)
            print("nuevo jugador:", nom)
        else:
            print("el servidor esta lleno")

    def stacksJugadores(self):
        i = 0
        while i < len(self.__jugadores):
            stacks = self.__diamantes[i] // 64
            print(self.__jugadores[i], "tiene", stacks, "stacks de diamantes")
            i = i + 1

    def jugadorMasDiamantes(self):
        if len(self.__jugadores) == 0:
            print("no hay jugadores")
            return
        maxdiam = self.__diamantes[0]
        pos = 0
        i = 1
        while i < len(self.__diamantes):
            if self.__diamantes[i] > maxdiam:
                maxdiam = self.__diamantes[i]
                pos = i
            i = i + 1
        print("jugador con más diamantes:", self.__jugadores[pos])

    def totalDiamantes(self):
        total = 0
        i = 0
        while i < len(self.__diamantes):
            total = total + self.__diamantes[i]
            i = i + 1
        print("total de diamantes:", total)

server = ServidorMinecraft()
n = int(input("jugadores a agregar: "))
i = 0
while i < n:
    nombre = input("nombre: ")
    diam = int(input("diamantes: "))
    server.agregarJugador(nombre, diam)
    i = i + 1
server.stacksJugadores()
server.jugadorMasDiamantes()
server.totalDiamantes()