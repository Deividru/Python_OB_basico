class Vehiculo:

    nombre = ""
    precio = 0.0
    caballos = 0

    def __init__(self,nombre,precio,caballos):
            self.nombre=nombre
            self.precio=precio
            self.caballos=caballos

    def getnombre(self,nombre):

            return self.nombre

    def imprimehola(self):
        return print("hola")

