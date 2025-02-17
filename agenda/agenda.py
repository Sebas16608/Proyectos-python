agenda = {
    "Jose": 302944,
    "Mario": 829455,
    "Angel": 829405,
    "Luis": 930594
}

consultar = True

while consultar:
    print()
    print("MI AGENDA")
    print("----------------------------")
    print("1. Consultar \n2. Añadir \n3. Modificar \n4. Borrar \n5. Salir")

    opcion = input("-> ")

    while opcion not in ("1", "2", "3", "4", "5"):
        print("Opción no válida, por favor elige una opción correcta.")
        opcion = input("-> ")

    if opcion == "1":
        # Pedir nombre
        nombre = input("Nombre: ")
        # Ver si el nombre está en el diccionario
        if nombre not in agenda:
            print("Este nombre no existe :(")
        else:
            telefono = agenda[nombre]
            print(f"{nombre} : {telefono}")

    elif opcion == "2":
        # Pedir nombre
        nombre = input("Nombre: ")
        if nombre in agenda:
            print("Este nombre ya está en la agenda")
        else:
            telefono = int(input("Escribe el teléfono: "))
            # Añadir el teléfono agendado
            agenda[nombre] = telefono
            print("El número se ha registrado con éxito :D")

    elif opcion == "3":
        nombre = input("Nombre: ")
        if nombre not in agenda:
            print("Ese nombre no existe en la agenda")
        else:
            telefono = int(input("Escribe el número: "))
            agenda[nombre] = telefono
            print("El número se ha modificado exitosamente")

    elif opcion == "4":
        nombre = input("Nombre: ")
        if nombre not in agenda:
            print("El nombre no está guardado en la agenda")
        else:
            del agenda[nombre]
            print("El nombre se ha borrado con éxito")

    elif opcion == "5":
        consultar = False
        print("Gracias por usar la agenda, ¡hasta luego! :D")