class Libro:
    def __init__(self, nombre, autor, año):
        self.nombre = nombre
        self.autor = autor
        self.anio = año

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Autor:", self.autor)
        print("Año:", self.año)


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cantLibros = 0
        self.libros = []

    def agregarLibro(self, libro):
        if self.cantLibros < 100:
            self.libros.append(libro)
            self.cantLibros + self.cantLibros + 1

    def buscarLibro(self, nombreLibro):
        for libro in self.libros:
            if libro.nombre == nombreLibro:
                print("Libro encontrado en", self.nombre)
                libro.mostrar()
                return
        print("Libro no encontrado en", self.nombre)

    def mostrarBiblioteca(self):
        print("\n Biblioteca:", self.nombre)
        print("Cantidad de libros:", self.cantLibros)


b1 = Biblioteca("Central")
b2 = Biblioteca("Escolar")

b1.agregarLibro(Libro("Naci para esto", "Alice Oseman", 2018))
b1.agregarLibro(Libro("Asesino de Brujas", "Shelby Mahurin", 2021))

b2.agregarLibro(Libro("El príncipe cruel", "Holly Black", 2020))
b2.agregarLibro(Libro("El caliz de los dioses", "Rick Riordan", 2023))

b1.buscarLibro("1984")
b2.buscarLibro("Dracula")

if b1.cantLibros > b2.cantLibros:
    b1.mostrarBiblioteca()
elif b2.cantLibros > b1.cantLibros:
    b2.mostrarBiblioteca()
else:
    b1.mostrarBiblioteca()
    b2.mostrarBiblioteca()