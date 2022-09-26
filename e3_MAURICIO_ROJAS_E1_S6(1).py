#Ejercicio 1
import random as rd

#1.
arregloA=[0]*100;
for i in range(len(arregloA)):
    arregloA[i]=rd.randrange(500)
print(arregloA)

#2. Indices pares
for i in range(len(arregloA)):
    if i%2==0:
        #print(f"{i}{arregloA[i]}")
        print("\nel indice par con su respectivo elemento es:",i,arregloA[i])

#3.Muestra mayor elemento del arreglo

mayor=arregloA[0]
for i in arregloA:
    if (i>mayor):
        mayor=i
print("\nEl elemento mayor es:",mayor)

#4. Muestra el indice (posicion) del elemento mayor del arreglo
mayor=0
indice=0
for i in range(len(arregloA)):
    if (arregloA[i]>mayor):
        mayor=arregloA[i]
        indice=i
print("\nel indice del elemento mayor es:",indice)

#5. Muestra el elemento menor del arreglo
menor=500
indice=0
for i in range(len(arregloA)):
    if (arregloA[i]<menor):
        menor=arregloA[i]
        indice=i
print("\nel indice del elemento menor del arreglo es:",indice)
print("\nEl elemento menor del arreglo es:",menor)

#6. Genera la copia del Arreglo A y multiplicar por 3 cada elemento. Mostrar resultado

copia_arregloA=arregloA[:].copy()
print(copia_arregloA)

for i in range(len(copia_arregloA)):
    copia_arregloA[i]=copia_arregloA[i]*3
print("\nAl multiplicar la copia de arreglo A se tiene:",copia_arregloA)

#7. Muestra la suma de los elementos del segundo arreglo.

suma_segundo_arreglo=0
for i in range(len(copia_arregloA)):
    suma_segundo_arreglo=suma_segundo_arreglo+copia_arregloA[i]
print("\nLa suma de todos los elementos del segundo arreglo (copia del arreglo A) es:",suma_segundo_arreglo)

#8. Calcula el promedio de los elementos del segundo arreglo.
promedio=(suma_segundo_arreglo/len(copia_arregloA))
print("\nEl promedio de los elementos del segundo arreglo es:\n",promedio)