import time

def main():
   hora=19
   min=00
   #hora = int(input("introduzca la hora de salida: "))
   #min  = int(input("introduzca los minutos de la hora de salida: "))

   l = time.localtime()

   print("Actualmente es : ",time.ctime(),"\n")

   check(l,hora,min)

def check(l,hora,min):

   if l.tm_hour < hora or (l.tm_hour== hora and l.tm_min < min):

      print("Aun no es la hora de salida (", hora, "h :",min, "m )\n")

      if l.tm_min == min:
         print("Quedan ", hora - l.tm_hour, "horas", 0, "minutos")
      else:
         if l.tm_min < min:
            print("Quedan ",abs(l.tm_hour - (hora)), "horas", (min - l.tm_min), "minutos","para la hora de salida")
         else:
            print("Quedan ", abs(l.tm_hour - (hora -1)), "horas", abs(60 + min - l.tm_min), "minutos","para la hora de salida")
   else:

      if l.tm_hour > hora or (l.tm_hour== hora and l.tm_min > min):
         print("La hora introducida como salida es anterior a la actual por lo que ya puedes irte")
      else:
         print("es Exactamente la hora de salida")


main()


