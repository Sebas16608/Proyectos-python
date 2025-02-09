nombre = input("Ingrese su nombre: ")
valor_compra = float(input("Ingrese el precio de su compra: "))

if valor_compra < 80:
    descuento = 0  # No hay descuento si la compra es menor a 80
    print(f"Hola {nombre} el precio a pagar es {valor_compra}")
elif valor_compra >= 80 and valor_compra < 150:
    descuento = 0.1
elif valor_compra >= 150 and valor_compra < 300:
    descuento = 0.15
elif valor_compra >= 300 and valor_compra < 500:
    descuento = 0.20
else:
    descuento = 0.25

precio_final = valor_compra - (valor_compra * descuento)
if valor_compra >80:
    print(f"Hola {nombre}")
    print(f"El precio sin descuento es: {valor_compra} USD")
    print(f"El precio con descuento es: {precio_final} USD")