#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
e = int(input("ingrese su edad actual: "))
if e >= 18:
    print("es mañor de edad")
else:
    print("es menor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

n = int(input("Ingrese su nota: "))
if n >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

n = int(input("ingrese un numero: "))
if n % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

c = int(input("ingrese su edad: "))
if c < 12:
    print("Niño/a")
elif c < 18:
    print("Adolescente")
elif c < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

c = (input("ingrese una contraseña: "))
if 8 <= len(c) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
#y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
#siguiente:
#from statistics import mode, median, mean
#mi_lista = [1,2,5,5,3]
#mean(mi_lista)
#En la documentación oficial se puede encontrar más información sobre este paquete:
#https://docs.python.org/es/3.8/library/statistics.html.
#La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
#pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
#● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
#mediana es mayor que la moda.
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
#la mediana es menor que la moda.
#● Sin sesgo: cuando la media, la mediana y la moda son iguales.
#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma:
#import random
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
#forma aleatoria.

import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
from statistics import mode, median, mean
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if media > mediana > moda:#    print("sesgo positivo")
elif media < mediana < moda:
    print("sesgo negativo")
else:
    print("sin sesgo")


#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

p = (input("ingrese una frase o una palabra: "))
if p[-1] in "aeiou":
    print(f"{p}!")
else:
    print(f"{p}")

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nom = (input("ingrese su nombre: "))
num = int(input("Si quiere su nombre en mayúsculas ingrese 1.\nSi quiere su nombre en minúsculas ingrese 2\nSi quiere su nombre con la primera letra mayúscula. ingrese 3.\ningrese un numero: "))
if num == 1:
    print(nom.upper())
elif num == 2:
    print(nom.lower())
elif num == 3:
    print(nom.title())
else:
    print("intentelo de nuevo.")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

t = int(input("ingrese la magnitud de un terremoto: "))
if t < 3:
    print("Muy leve (imperceptible).")
elif t < 4:
    print("Leve (ligeramente perceptible).")
elif t < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif t < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif t < 7:
    print("Muy fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")

#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año.
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

# Pedimos los datos al usuario
hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

# Convertimos el mes y el día en una "posición" del año para comparar más fácil
# Ejemplo: 21 de marzo -> (3, 21)
# Hacemos las comparaciones según la tabla

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"

elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"

elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"

elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"

# Mostramos la estación según el hemisferio
if hemisferio == "N":
    print(f"Estás en el hemisferio norte. La estación es {estacion_norte}.")
elif hemisferio == "S":
    print(f"Estás en el hemisferio sur. La estación es {estacion_sur}.")
else:
    print("Hemisferio no reconocido. Usá 'N' o 'S'.")
