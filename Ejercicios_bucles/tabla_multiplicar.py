print("Hoy escribiremos las tablas. Por favor ingrese lo que se le pide \n")

num = int(input("Ingrese el numero: "))

for i in range(1,11):
    resultado = num * i
    print(f"{num} X {i} = {resultado}")