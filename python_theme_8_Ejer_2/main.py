import pickle

from Vehiculo import *

if __name__=="__main__":

    #creamos un objeto de la clase vehiculo
    #al cual instanciamos con un nombre y lo modificamos despues.
    c1 = Vehiculo("ferrari",10045,190)
    print(c1.nombre)
    print("contiene ", c1.caballos)
    c1.nombre = "seat"

    # creamos un nuevo documento para almacenar el objeto usamos wb para poder escribir .
    doc = open("datos.bin", "wb")
    pickle.dump(c1, doc)


    # creamos un nuevo documento para almacenar el objeto usamos rb para poder leer .
    doc = open("datos.bin", "rb")
    # guardamos el contenido del objeto en la variable f
    f = pickle.load(doc)

    doc.close()

    print("nuestro coche mantiene su nombre despues del cambio ", f.nombre)


