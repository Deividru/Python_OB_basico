

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

if __name__ == '__main__':
    print('PyCharm mi primer ejercicio en python')

    while 1:
        try:
            a = int(input(" Inserte su Edad :  "))
            print(" su edad es: " + str(a))
            print(" comprobaremos si usted es mayor de edad: " )

            if a >= 18:
                print("Enhorabuena usted puede acceder al contenido")
                break
            else:
                print("Lo sientimos usted no tiene la edad suficiente para continuar.")
                break
        except:

            print("Introduzca un número, el programa se volvera a preguntar.")



