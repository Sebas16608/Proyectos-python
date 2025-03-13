def dolares(a):
    return a * 0.13
def euros(a):
    return a * 0.12
def pesosmx(a):
    return a*2.61

while True:
    print("\nHola bienvenido al conversor de monedas, por favor ingrese lo que se le pide en quetzales \n")
    print("Elija una opcion \n")
    print("1. Convertir Quetzales a Dólares.")
    print("2. Convertir Quetzales a Euros.")
    print("3. Convertir Quetzales a Pesos Mexicanos")
    print("4. Salir.")
    opcion = int(input("\nElija una opción: "))

    if opcion == 4:
        print("\nGracias por usar el conversor.")
        break 
    if opcion in [1, 2, 3]: #lo usaremos para no poner moeda en todas las opciones que hay
        moneda = float(input("Ingrese la cantidad de dinero en Quetzales: "))
        if opcion == 1:
            print(f"La cantidad es de {moneda} quetzal/es a dólares es {dolares(moneda):.2f} USD.")
        elif opcion == 2:
            print(f"La cantidad es de {moneda} quetzal/es a euros es {euros(moneda):.2f} EUR.")
        elif opcion == 3:
            print(f"La cantidad es de {moneda} quetzal/es a pesos mexicanos es {pesosmx(moneda):.2f} MXN. ")
    else:
        print("Opción no valida.")