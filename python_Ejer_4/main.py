import math

if __name__== '__main__':

     print("Ejercicio 4 python funciones")

     def areaTriangulo(altura,base):

          return (base*altura)/2

     def areaCirculo(radio):

          return (math.pi * (radio**2))

     a = float (input(" inserten la altura del triangulo en cuestion:  "))
     b = float (input(" ahora inserte la base del triangulo:  "))

     areaT = areaTriangulo(a,b)

     print('area de un triangulo de base ' + str(b) + ' y de altura' + str(a) +' es : ' + str(areaT))

     r = float(input(" inserten el radio del ciurculo en cuestion:  "))

     areaC = round(areaCirculo(r),3)

     print('area de un Circulo de radio ' + str(r) + ' es de : ' + str(areaC))

