print("Hola, hoy vamos a convertir grados Centigrados a grados Fahrenheit \n")
print("Ingrese los datos correspondientes, por favor \n")

#pedimos datos
cen = float(input("Ingrese el grado centigrado: "))

#calculamos los grados a Fahrenheit
fahr = (cen * 9/5)+32

#imprimimos el resultado
print(f"El grado que ingreso es: {cen} y pasado a Fahrenheit seria: {fahr}")
