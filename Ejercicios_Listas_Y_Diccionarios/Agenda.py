# Diccionario con base de datos
agenda = {
    "Mario": 55689078,
    "Juan": 30085258,
    "Pedro": 5548975,
    "Maria": 53647890 
}

consultar = True

# Usando un bucle while para poder pedirle al usuario cuantas veces quiera hacer lo que necesite
while consultar:
    print("Agenda Telefónica \n")
    print("--------------------------")
    print("1. Consultar \n2. añadir \n3. Modificar \n4. Borrar \n5. Salir")

    opcion = input("-> ")

    while opcion not in ("1", "2", "3", "4", "5"):
        print("Opción no válida, por favor elige una opción correcta.")
        opcion = input("-> ")
    # es la parte de consultas osea la opcion 1
    if opcion == "1":
        # pedir nombre
        name = input("Ingrese el nombre: ")
        # verificar si el nombre esta en el diccionario
        if name not in agenda:
            print("Nombre no disponible")
        else:
            telefono = agenda[name]
            print(agenda[name], agenda[telefono])
    # es la parte para añadir osea la opcion 2
    elif opcion == "2":
        name = input("Nombre: ")
        if name in agenda:
            print("Nombre ya registrado")
        else:
            telefono = int(input("Numero: "))
            # añadir el telefono agregado recientemente
            agenda[name] = telefono
            print("Registrado exitosamente.")
    elif opcion == "3":
        name = input("Nombre: ")
        if name not in agenda:
            print("El nombre no esta en la agenda para poder modificarlo.")
        else:
            telefono = int(input("Numero: "))
            # Añadir el nuevo numero a la agenda
            agenda[name] = telefono
            print("Numero modificado exitosamente.")
    elif opcion == "4":
        name = input("Nombre: ")
        if name not in agenda:
            print("El nombre no esta en la agenda")
        else:
            del agenda[name]
            print("El Contacto se ha eliminado correctamente")

    elif opcion == "5":
        consultar = False
        print("Gracias por utilizar la agenda :D hasta pronto...")