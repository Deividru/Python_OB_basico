



if __name__== '__main__':

    class Alumno():
        IDalumno = 1

        def __init__(self, nota, nombre):
            self.nota = nota;
            self.nombre = nombre;
            Alumno.IDalumno= 200

        def aprobado(self):
            if self.nota > 5: print("el alumno a " + david.nombre + " ha aprobado ?  " +str(david.nota))
            else: print("el alumno a " + david.nombre + " Ha SUSPENDID0 con un  " +str(david.nota))



david = Alumno(8,"David Rubiano")

david.aprobado()





