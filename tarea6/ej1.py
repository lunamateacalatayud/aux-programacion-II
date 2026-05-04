# ejercicio 4
# agregacion - composicion
# Calatayud Luna Mariana
class Mueble:
    def __init__(self, tipo, material):
        self.tipo = tipo
        self.material = material

    def __str__(self):
        return f"{self.tipo} - {self.material}"


class Habitacion:
    def __init__(self, nombre, tamanio):
        self.nombre = nombre
        self.tamanio = tamanio
        self.muebles = []

    def agregarMueble(self, mueble):
        self.muebles.append(mueble)

    def cantMuebles(self):
        return len(self.muebles)

    def __str__(self):
        return f"Habitación: {self.nombre}, Muebles: {len(self.muebles)}"


class Departamento:
    def __init__(self, nroPuerta, nroPiso):
        self.nroPuerta = nroPuerta
        self.nroPiso = nroPiso
        self.habitaciones = []

    def agregarHabitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def cantHabitaciones(self):
        return len(self.habitaciones)

    def totalMuebles(self):
        total = 0
        for h in self.habitaciones:
            total = total + h.cantMuebles()
        return total

    def habitacionConMasMuebles(self):
        if len(self.habitaciones) == 0:
            return None

        mayor = self.habitaciones[0]
        for h in self.habitaciones:
            if h.cantMuebles() > mayor.cantMuebles():
                mayor = h
        return mayor

    def __str__(self):
        return f"Depto Puerta {self.nroPuerta} Piso {self.nroPiso}"


class Parqueo:
    def __init__(self, capacidad, precioH):
        self.capacidad = capacidad
        self.precioH = precioH
        self.autos = []

    def agregarAuto(self, placa):
        if len(self.autos) < self.capacidad:
            self.autos.append(placa)
            print("auto agregado al parqueo.")
        else:
            print("no hay capacidad disponible en el parqueo.")

    def __str__(self):
        return f"Parqueo: {len(self.autos)}/{self.capacidad}"


class Edificio:
    def __init__(self, nombre, superficie):
        self.nombre = nombre
        self.superficie = superficie
        self.departamentos = []
        self.parqueo = None

    def adicionarParqueo(self, parqueo):
        self.parqueo = parqueo

    def agregarDepartamento(self, depto):
        self.departamentos.append(depto)

    def deptoMasHabitacionesPiso(self, piso):
        mayor = None
        for d in self.departamentos:
            if d.nroPiso == piso:
                if mayor is None or d.cantHabitaciones() > mayor.cantHabitaciones():
                    mayor = d
        return mayor

    def agregarMuebleADepartamento(self, piso, puerta, nombreHab, mueble):
        for d in self.departamentos:
            if d.nroPiso == piso and d.nroPuerta == puerta:
                for h in d.habitaciones:
                    if h.nombre == nombreHab:
                        h.agregarMueble(mueble)
                        return True
        return False

    def deptosConMasMuebles(self):
        mayor = 0

        for d in self.departamentos:
            if d.totalMuebles() > mayor:
                mayor = d.totalMuebles()

        for d in self.departamentos:
            if d.totalMuebles() == mayor:
                print(d)

    def habitacionMasMueblesPiso(self, piso):
        mayorHab = None

        for d in self.departamentos:
            if d.nroPiso == piso:
                hab = d.habitacionConMasMuebles()

                if hab is not None:
                    if mayorHab is None or hab.cantMuebles() > mayorHab.cantMuebles():
                        mayorHab = hab

        return mayorHab

    def eliminarDeptosHabitacionesPrimas(self):
        nuevos = []

        for d in self.departamentos:
            if not self.esPrimo(d.cantHabitaciones()):
                nuevos.append(d)
        self.departamentos = nuevos

    def esPrimo(self, n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True



ed = Edificio("Torre Luna", 5000)
parq = Parqueo(3, 10)
ed.adicionarParqueo(parq)
d1 = Departamento(101, 1)
d2 = Departamento(102, 1)
h1 = Habitacion("Dormitorio", 20)
h2 = Habitacion("Sala", 30)
h3 = Habitacion("Cocina", 15)
h1.agregarMueble(Mueble("Cama", "Madera"))
h1.agregarMueble(Mueble("Ropero", "Metal"))
h2.agregarMueble(Mueble("Sofá", "Cuero"))
d1.agregarHabitacion(h1)
d1.agregarHabitacion(h2)
d2.agregarHabitacion(h3)
ed.agregarDepartamento(d1)
ed.agregarDepartamento(d2)
print(ed.deptoMasHabitacionesPiso(1))
ed.agregarMuebleADepartamento(1, 101, "Sala", Mueble("Mesa", "Vidrio"))
ed.deptosConMasMuebles()
print(ed.habitacionMasMueblesPiso(1))
ed.eliminarDeptosHabitacionesPrimas()
ed.parqueo.agregarAuto("123ABC")
ed.parqueo.agregarAuto("456DEF")
ed.parqueo.agregarAuto("789XYZ")
ed.parqueo.agregarAuto("999ZZZ")
