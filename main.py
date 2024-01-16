# Ejercicio 1
lista_primer_ejercicio = [x ** 2 for x in range(1, 101)]
# Ejercicio 2
lista_segundo_ejercicio = [x for x in range(1, 21) if x % 2 == 0]
#Ejercicio 3
lista_tercer_ejercicio = [x for x in range(1, 101) if x % 3 == 0]
#Ejercicio 4
lista_cuarto_ejercicio = [x for x in range(100, 0, -1)]
#Ejercicio 5
lista_quinto_ejercicio = [x ** 2 for x in range(1, 101) if x % 3 != 0]
# Crea un diccionario que contenga los números del 1 al 10 como claves y sus cuadrados como valores.
lista_numeros_1 = [x for x in range(1, 10)]
diccionario_ejercicio_1 = {numero: numero ** 2 for numero in lista_numeros_1}
print(diccionario_ejercicio_1)
# Crea un diccionario que contenga las letras del alfabeto como claves y su número correspondiente en el código ASCII como valores.
lista_numeros_ASCII = [x for x in range(97, 122)]
diccionario_ejercicio_2 = {chr(numero): numero for numero in lista_numeros_ASCII}
print(diccionario_ejercicio_2)

