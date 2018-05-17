import time
hora = 0
min = 0
seg = 0
ho = int(input("Ingrese la hora del temporizador: "))
mi = int(input("Ingrese los minutos del temporizador: "))
se = int(input("Ingrese los segundos del temporizador: "))
while True:
    for x in range(1,60):
        print(hora,':',min,x)
        #time.sleep(1)
        if hora == ho and min == mi and x == se:
           print('---------Alarma---------')
           exit()
        if x==59:
            min=min+1
            x=0
        if min==60:
            hora=hora+1
            min=0
            x=0
        if hora>=25 or min>60 or seg>59:
            exit()
        if ho>=25 or mi>59 or se>59 :
            print('----Datos mal ingresados---')
            exit()
        if se==0:
           print('----segundo 0 no existe---')
           exit()




