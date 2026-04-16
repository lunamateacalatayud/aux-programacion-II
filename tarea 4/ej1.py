# ejercicio 3
# Luna Mariana Calatayud
class Persona:
    def __init__(self, nombre, carnet, edad):
        self.nombre = nombre
        self.carnet = carnet
        self.edad = edad

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Carnet: {self.carnet}, Edad: {self.edad}")


class Estudiante(Persona):
    def __init__(self, nombre, carnet, edad, matricula, carrera):
        super().__init__(nombre, carnet, edad)
        self.matricula = matricula
        self.carrera = carrera

    def mostrar(self):
        super().mostrar()
        print(f"Matrícula: {self.matricula}, Carrera: {self.carrera}")


class Docente(Persona):
    def __init__(self, nombre, carnet, edad, antiguedad, sueldo):
        super().__init__(nombre, carnet, edad)
        self.antiguedad = antiguedad
        self.sueldo = sueldo

    def mostrar(self):
        super().mostrar()
        print(f"Antigüedad: {self.antiguedad}, Sueldo: {self.sueldo}")


e1 = Estudiante("Ana", 123, 20, 1001, "Sistemas")
e2 = Estudiante("Luis", 456, 25, 1002, "Industrial")
d1 = Docente("Carlos", 789, 25, 10, 3500)

print("Estudiante 1")
e1.mostrar()
print("-----")

print("Estudiante 2")
e2.mostrar()
print("-----")

print("Docente")
d1.mostrar()
print("-----")


if e1.edad == d1.edad or e2.edad == d1.edad:
    print("Algún estudiante tiene la misma edad que el docente")
else:
    print("Ningún estudiante tiene la misma edad que el docente")


if e1.carrera == e2.carrera:
    print("Están en la misma carrera")
else:
    print("No están en la misma carrera")