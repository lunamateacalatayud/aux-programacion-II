# Luna Mariana Calatayud
# TAREA 7
# ejercicio 8: Excepciones personalizadas
class SueldoInvalidoException(Exception):
    pass

class CargoInvalido(Exception):
    pass

class Empleado:
    def __init__(self, nombre, cargo, sueldo):
        self.nombre = nombre
        self.cargo = cargo
        self.sueldo = sueldo

class Empresa:
    sueldoMinimo = 2500

    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def registrarEmpleado(self):
        nombre = input("Nombre: ")

        while True:
            cargo = input("Cargo: ")
            try:
                if any(c.isdigit() for c in cargo):
                    raise CargoInvalido("El cargo no puede contener números.")
                break
            except CargoInvalido as e:
                print(f"Error: {e} Intente de nuevo.")

        sueldo = float(input("Sueldo: "))
        try:
            if sueldo < self.sueldoMinimo:
                raise SueldoInvalidoException(f"Sueldo menor al mínimo ({self.sueldoMinimo} Bs).")
        except SueldoInvalidoException as e:
            print(f"{e} Se asigna sueldo mínimo automáticamente.")
            sueldo = self.sueldoMinimo

        self.empleados.append(Empleado(nombre, cargo, sueldo))
        print("Empleado registrado.\n")

    def mostrarEmpleados(self):
        print(f"\n Empleados de {self.nombre}")
        for i in range(len(self.empleados)):
            e = self.empleados[i]
            print(f"{e.nombre} | {e.cargo} | {e.sueldo} Bs")


empresa = Empresa(input("Nombre de la empresa: "))
n = int(input("¿Cuántos empleados va a registrar? "))

for i in range(n):
    print()
    empresa.registrarEmpleado()

empresa.mostrarEmpleados()
