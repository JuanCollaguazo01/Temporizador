import time

x= int (input("Ingrese el tiempo: "))

while True:
   if x==0:
      print ("---------TIEMPO---------")
      exit()
   else:
      x=x-1
      time.sleep(1)
      print (x)