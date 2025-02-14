print("Hola, vamos a calcular su IMC \n")
print("Ingrese los datos que se le piden por favor\n")

#pediremos los datos
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en Kilogramos: "))

IMC = round(peso/(altura**2), 2)
"""
esto de aca puede ser opcional ya que no nos brinda todos los datos necesarios a lo que queremos

print(f"Tu IMC es: {IMC}")
"""
#entonces tambien podemos hacer un condicional
if IMC < 18.5:
    print("Tienes bajo peso.")
elif IMC < 25:
    print("Tienes un peso normal.")
elif IMC < 30:
    print("Tienes sobrepeso.")
else:
    print("Tienes obesidad.")