import random

#creamos un numero random
numero=random.randint(1,100)

#pedimos al usuario un numero
num=int(input("Ingrese el numero: "))

#creamos una variable como un contador que se llame intentos
intentos=1

#creamos el bucle para ver en cuantos intentos lo va a lograr
while num != numero:
    if num < numero:
        print(f"El numero es mayor a {num} \n")
    else:
        print(f"El numero es menor a {num} \n")
    #pedir otro numero
    num=int(input("ingrese otro numero: "))
    intentos+=1
print(f"Exelente, lo has logrado en {intentos} intentos")