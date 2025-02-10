#Solicitar Información

name=input("Ingrese su nombre: ")
materias=5

#hacer un ciclo, pedir datos y sumar la calificacion
contador=1
sumatoria=0

while contador <= materias:
    nombre_materia=input("Ingresa el nombre de la ("+str(contador)+") materia ")
    calificacion=float(input("Calificacion obtenidas en "+str(nombre_materia)+": "))
    
    #aumentar el contador
    contador+=1

#sumar la calificacion a la sumatoria
sumatoria=sumatoria+calificacion

#hacer calculos he imprimir el resultado
promedio=sumatoria/materias
print("***RESULTADOS***")
print(f"Hola {name} tienes un promedio de {promedio} en el 5to semestre")