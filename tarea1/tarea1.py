class Anime:
    def __init__(self, nom, gen, nroEps):
        self.nombre = nom
        self.genero = gen
        self.nroEpisodios = nroEps
        self.episodios = []

    def agregarEpis(self, episodio):
        self.episodios.append(episodio)

    def __str__(self):
        return f"Anime: {self.nombre}, Género: {self.genero}, Episodios: {self.nroEpisodios}"


class Televisor:
    def __init__(self, marca="", resolucion=0, tipo=""):
        self.marca = marca
        self.resolucion = resolucion
        self.tipo = tipo

    def __str__(self):
        return f"Televisor: {self.marca}, Resolución: {self.resolucion}p, Tipo: {self.tipo}"


class Instrumento:
    def __init__(self, nombre, material, tipo):
        self._nombre = nombre
        self._material = material
        self._tipo = tipo

    def getNombre(self):
        return self._nombre

    def getMaterial(self):
        return self._material

    def getTipo(self):
        return self._tipo

    def setNombre(self, nombre):
        self._nombre = nombre

    def setMaterial(self, material):
        self._material = material

    def setTipo(self, tipo):
        self._tipo = tipo

    def __str__(self):
        return f"Instrumento: {self._nombre}, Material: {self._material}, Tipo: {self._tipo}"

class Main():
    anime1 = Anime("One Piece", "Aventura", 1155)
    anime2 = Anime("Dr Stone", "Ciencia", 60)

    tele1 = Televisor("Samsung", 1080, "LED")
    tele2 = Televisor("LG", 2160, "LED")

    inst1 = Instrumento("Violin", "Madera", "Cuerda")
    inst2 = Instrumento("Trompeta", "Metal", "Aire")

    print(anime1)
    print(anime2)
    print(tele1)
    print(tele2)
    print(inst1)
    print(inst2)
