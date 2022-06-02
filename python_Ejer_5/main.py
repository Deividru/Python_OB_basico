
if __name__== '__main__':
     print ("ejercicio 5 Números primos")
     def nprimo(a):
          compuesto = 0
          lista=[]
          for i in range (2,a):
               if a % i == 0:
                    compuesto= compuesto + 1
                    lista.append(i)

          if compuesto == 0 :
               print(" El numero " +str(a) + " es un numero primo")
          else:
               print(" El numero: [" + str(a) + "] es divisible por " +str(compuesto) + " números")
               print(lista)

     a = int(input("Inserte un numero entero acontinuación:  "))
     #a = 100

     nprimo(a)

