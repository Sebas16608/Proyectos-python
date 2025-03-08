def factorial(a):
    resultado = 1
    for i in range(1, a+1):
        resultado *= i
    return resultado


print("Hola, ingrese un numero para sacar su factorial")

num = int(input("\n ingrese el numero: "))

print(f"El factorial del numero {num} es {factorial(num)}")