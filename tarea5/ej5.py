class Animal:
    def __init__(self, nombre, edad, nombreDueño):
        self.nombre = nombre
        self.edad = edad
        self.nombreDueño = nombreDueño


class Perro(Animal):
    def __init__(self, nombre, edad, nombreDueño, requiereBosal, ladraFuerte):
        super().__init__(nombre, edad, nombreDueño)
        self.requiereBosal = requiereBosal
        self.ladraFuerte = ladraFuerte


class Gato(Animal):
    def __init__(self, nombre, edad, nombreDueño, cazaRatas, tomaLeche):
        super().__init__(nombre, edad, nombreDueño)
        self.cazaRatas = cazaRatas
        self.tomaLeche = tomaLeche


class CentroVeterinario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.perros = []
        self.gatos = []

    def agregarPerro(self, perro):
        if len(self.perros) < 100:
            self.perros.append(perro)

    def agregarGato(self, gato):
        if len(self.gatos) < 100:
            self.gatos.append(gato)

    def ordenarPerros(self):
        n = len(self.perros)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                cambiar = False
                if self.perros[j].edad > self.perros[j + 1].edad:
                    cambiar = True
                elif self.perros[j].edad == self.perros[j + 1].edad:
                    if self.perros[j].nombreDueño > self.perros[j + 1].nombreDueño:
                        cambiar = True
                    elif self.perros[j].nombreDueño == self.perros[j + 1].nombreDueño:
                        if self.perros[j].nombre > self.perros[j + 1].nombre:
                            cambiar = True
                if cambiar:
                    aux = self.perros[j]
                    self.perros[j] = self.perros[j + 1]
                    self.perros[j + 1] = aux


    def ordenarGatos(self):
        n = len(self.gatos)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                cambiar = False
                if self.gatos[j].tomaLeche == False and self.gatos[j + 1].tomaLeche == True:
                    cambiar = True
                elif self.gatos[j].tomaLeche == self.gatos[j + 1].tomaLeche:
                    if self.gatos[j].edad < self.gatos[j + 1].edad:
                        cambiar = True
                    elif self.gatos[j].edad == self.gatos[j + 1].edad:
                        if self.gatos[j].nombre > self.gatos[j + 1].nombre:
                            cambiar = True
                if cambiar:
                    aux = self.gatos[j]
                    self.gatos[j] = self.gatos[j + 1]
                    self.gatos[j + 1] = aux


    def verificarDueñoRepetido(self):
        todos = self.perros + self.gatos
        for i in range(len(todos)):
            contador = 1
            for j in range(i + 1, len(todos)):
                if todos[i].nombreDueño == todos[j].nombreDueño:
                    contador = contador + 1
            if contador > 1:
                print(todos[i].nombreDueño, "tiene", contador, "animales")
                return



cv1 = CentroVeterinario("Patitas")
cv2 = CentroVeterinario("Mascotitas")

cv1.agregarPerro(Perro("Max", 5, "Ana", True, True))
cv1.agregarPerro(Perro("Rocky", 3, "Luis", False, False))
cv1.agregarGato(Gato("Michi", 2, "Ana", True, True))
cv1.agregarGato(Gato("Pelusa", 4, "Pedro", False, False))

cv2.agregarPerro(Perro("Thor", 6, "Mario", True, True))
cv2.agregarPerro(Perro("Boby", 1, "Sofia", False, True))
cv2.agregarGato(Gato("Pelusa", 5, "Mario", True, False))
cv2.agregarGato(Gato("Nina", 3, "Lucia", False, True))

cv1.ordenarPerros()
cv1.ordenarGatos()

cv1.verificarDueñoRepetido()
cv2.verificarDueñoRepetido()