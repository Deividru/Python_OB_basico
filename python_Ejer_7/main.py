

if __name__== '__main__':

    class Vehiculo:

        color = "BLanco"
        ruedas = 4
        puertas = 5


    class Coche(Vehiculo):

        velocidad = 300
        cilindrada = 2500


    a = Coche()

    print("color : " + a.color)
    print("ruedas : " + str(a.ruedas))
    print("puertas : " + str(a.puertas))
    print("velocidad : " + str(a.velocidad))
    print("cilindrada : " + str(a.cilindrada))