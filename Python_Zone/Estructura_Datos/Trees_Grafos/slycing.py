fruta = "Naranja"
for car in fruta:
    print(car)
print("\n")

#-------------------------------------------
s = "Montypython"
len(s)  # 12
print(s[0:5])  # Monty
print(s[5:12])  # python
print("\n")

#-------------------------------------------
fruta2 = "Banana"
print(len(fruta2))
print(fruta2[:3])
print(fruta2[3:])
#fruta2[0] = "b" es inmutable, no puede cambiarse
print("\n")

#-------------------------------------------
fruta3 = "b"+fruta2[1:] #aquí si es mutable
print(fruta3)
print("\n")
#-------------------------------------------
fruta4 = "La Naranja es Rica en Vitamina C"
print(fruta4)  # naranja
print(fruta4.upper())  # naranja
print(fruta4.lower())  # naranja
print(fruta4.isdigit())  # Naranja
print(fruta4.isalpha())  # Naranja
#-------------------------------------------
print(fruta4.split(' '))  # Lo vuelve una lista de palabras
print("\n")

#-------------------------------------------
#Arrays/Listas "M"
lista = fruta4.split(' ')
#print(lista)
#lista[0]= 1 #modificar un elemento de la lista/cambios
#lista[1]= 2.0

#print(lista)
print(lista[:3])
print(lista[3:])

lista.append("y") #agregar un elemento al final de la lista
lista.append("Calcio")
print(lista)

lista.insert(2, "y")
lista.insert(3, "el")
lista.insert(4, "limon")
lista[5] = "son" #Modificacion directa
lista[6] = "ricos"
print(lista)
print("\n")

#-------------------------------------------
#Slicing
print(lista[:])  # Muestra los elementos de la posición 0 a la 2
