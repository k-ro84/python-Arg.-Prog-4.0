#Parte 1
#Resolver el siguiente ejercicio de programación
#El empleado llamado Juan cobró 300 dólares por mes desde enero a junio, 500 dólares de julio a octubre, y 700 dólares por mes en noviembre y en diciembre. 

#En base al escenario propuesto, se le solicita a los estudiantes que creen un pequeño programa que calcule el sueldo promedio del empleado Juan.
#Además, se debe indicar sí Juan se encuentra cobrando un sueldo bajo, normal o mejor de lo normal, considerando las siguientes pautas:

#a. Sueldo bajo: por debajo de 300 dólares.
#b. Sueldo normal:  entre 300 a 900.
#c. Sueldo mejor de lo normal: más de 900 dólares.

#Tip: se debe utilizar estructuras condicionales.
print("______________________________________________________________________________")
nombre=input(" Bienvenido ingrese el nombre del trabajador para corroborar identidad : ")
sueldo=int(input(" Ingrese el sueldo total anual del empleado : $ " ))

prom =float(sueldo/12)

print("su sueldo promedio anual es de : $ "+ str(prom))

if prom < 300:
    print(" Juan, su sueldo es bajo :( " )
elif prom >300 and prom < 900 :
    print(" Juan, su sueldo es normal :/ ")
else:
    print(" Juan, su sueldo mejor de lo normal :) ")

saludo=("Gracias por utilizar nuestros servicios")
print(saludo)
print("______________________________________________________________________________")
#crear archivo py, guardar(file guardar as o ctrl+s)
#como correr archivo: cd Desktop(o Escritorio segun la pc)
#despues ingresar python + nombre del archivo.py
