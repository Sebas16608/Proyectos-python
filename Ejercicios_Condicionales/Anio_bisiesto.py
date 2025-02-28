print("Hola, hoy le dire que año es bisiesto y que año no. \n")

anio = int(input("Ingrese el numero del año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"{anio} es un año bisiesto.")
else:
    print(f"{anio} no es un año bisiesto.")
