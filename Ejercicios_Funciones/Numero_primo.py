def primo(a):
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True

while True:
    print("\nVamos a ver si el número es primo o no")
    print("1. Verificar si un número es primo")
    print("2. Salir")
    opcion = input("Ingrese lo que desea hacer: ")
    
    if opcion == "2":
        print("Saliendo...")
        break
    elif opcion == "1":
        num = int(input("Ingrese el número: "))
        if primo(num):
            print(f"El número {num} es primo")
        else:
            print(f"El número {num} no es primo")
    else:
        print("Opción no válida. Por favor, ingrese 1 o 2.")