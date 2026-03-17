# ejercicio 5
# Luna Mariana Calatayud

class Aula:
    def __init__(self, nombre, piso, estudiantes):
        self.__nombre = nombre
        self.__piso = piso
        self.__estudiantes = estudiantes

    def mostrarDatos(self, estado=None):

        if estado is None:
            print("Aula:", self.__nombre)
            print("Piso:", self.__piso)
            print("Estudiantes y notas:")
            for e in self.__estudiantes:
                print(e[0], "-", e[1])
        else:
            for e in self.__estudiantes:
                if e[1] >= 51:
                    print(e[0], "- Aprobado")
                else:
                    print(e[0], "- Reprobado")

estudiantes = [
    ["Luis", 67],
    ["Aracely", 89],
    ["Carlos", 40]
]

aula1 = Aula("Aula A", 1, estudiantes)
aula1.mostrarDatos()
print()
aula1.mostrarDatos(True)