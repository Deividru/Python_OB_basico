


if __name__== '__main__':

    # un año es bisiesto si y solo si es divisible por 4
    # ademas debe ser divisible por 100 y por 400!
    # el primer año que se establecio fue el 1582 por el Papa GregorioXII

    def bisiesto(a):

        bisiesto = False

        if a > 1581 :
            if a % 4 == 0 :
                if a % 100 != 0: bisiesto = True
                else:
                    if a % 400 == 0: bisiesto = True
        else:
            print(" el primer año que se establecio como bisiesto fue el 1582 por el Papa GregorioXII ")

        return bisiesto

    while True:
        a = int(input("Introduzca el año que desea verificar mayor a 1582:  "))
        check = bisiesto(a)


        if check == True :
            print("El año: [" + str(a) + "] Es bisiesto")
        else:
            if a >= 1582: print("El año: [" + str(a) + "] NO es bisiesto")




