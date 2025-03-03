print("Vamos a sumar todos los números desde 1 hasta N. Ingrese el valor de N.\n")

N = int(input("Introduce un número N: "))
suma = 0

for i in range(1, N + 1):
    suma += i

print(f"La suma desde 1 hasta {N} es: {suma}")