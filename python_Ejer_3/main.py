
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

if __name__ == '__main__':
    print("Ejercicio 2")

    #introducimos los valores

    a = int(input(" Introduzca el primer digito:  "))
    b = int(input(" Introduzca el Segundo digito:  "))

    print(" a continuacion veremos los numers impares entre el :" +str(a) + " y el : " + str(b))

    lista=[]

    for i in range(a,b+1):
        if i % 2 != 0:
            lista.append(i)

    print(lista)



