# Diccionario con base de datos
agenda = {
    "Mario": 55689078,
    "Juan": 30085258,
    "Pedro": 5548975,
    "Maria": 53647890 
}

contador = True

# Usando un bucle while para poder pedirle al usuario cuantas veces quiera hacer lo que necesite
while True:
    print("Agenda Telefónica \n")
    print("--------------------------")
    print("1. Consultar \n2. añadir \n3. Modificar \n4. Borrar \n5. Salir")

    opcion = int(input("-> "))

    while opcion not in ("1", "2", "3", "4", "5"):
        print("Opcion no valida elija la opcion correcta")
        opcion = int(input("->"))

    # es la parte de consultas osea la opcion 1
    if opcion == 1:
        # pedir nombre
        name = input("Ingrese el nombre: ")
        # verificar si el nombre esta en el diccionario
        if name not in agenda:
            print("Nombre no disponible")
        else:
            telefono = agenda[name]
            print(agenda[name], agenda[telefono])
    # es la parte para añadir osea la opcion 2
    elif opcion == 2:
        name = input("Nombre: ")
        if name in agenda:
            print("Nombre ya registrado")
        else:
            telefono = int(input("Numero: "))
            # añadir el telefono agregado recientemente
            agenda[name] = telefono
            print("Registrado exitosamente.")
    elif opcion == 3:
        name = input("Nombre: ")
        if name not in agenda:
            print("El nombre no esta en la agenda para poder modificarlo.")
        else:
            telefono = int(input("Numero: "))
            # Añadir el nuevo numero a la agenda
            agenda[name] = telefono
            print("Numero modificado exitosamente.")