print("Hola, hoy vamos a ver si aprueba o no. Por favor ingrese los datos que se le piden \n")

curso = input("Ingrese el nombre del curso: ")
num = float(input("Ingrese el punteo: "))

if num >= 60:
    print(f"Ha aprobado el curso de {curso} con una calificacion de {num}")
else:
    print(f"No ha aprobado el curso, lo siento")