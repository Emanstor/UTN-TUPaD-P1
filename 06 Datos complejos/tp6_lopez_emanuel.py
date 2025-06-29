# Autor: Lopez Emanuel
# Trabajo Práctico 6: Estructuras de datos complejas (sin objetos)
# Materia: Programación 1 - Tecnicatura Universitaria en Programación

# 1) Diccionario de precios de frutas - Agregar frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2) Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3) Lista con los nombres de las frutas
lista_frutas = list(precios_frutas.keys())
print("Lista de frutas:", lista_frutas)

# 4) Agenda de contactos
agenda = {}
for _ in range(5):
    nombre = input("Ingresá el nombre del contacto: ")
    telefono = input(f"Ingresá el número de {nombre}: ")
    agenda[nombre] = telefono

consulta = input("Ingresá el nombre para consultar su número: ")
if consulta in agenda:
    print(f"Número de {consulta}: {agenda[consulta]}")
else:
    print("Contacto no encontrado.")

# 5) Palabras únicas y cantidad de repeticiones
frase = input("Ingresá una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

conteo_palabras = {}
for palabra in palabras:
    conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1
print("Frecuencia de palabras:", conteo_palabras)

# 6) Promedio de notas de 3 alumnos
alumnos = {}
for _ in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(float(input(f"Ingresá nota {i+1} de {nombre}: ")) for i in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {nombre}: {promedio:.2f}")

# 7) Sets de alumnos que aprobaron
parcial1 = {input("Alumno que aprobó Parcial 1: ") for _ in range(3)}
parcial2 = {input("Alumno que aprobó Parcial 2: ") for _ in range(3)}

print("Aprobaron ambos parciales:", parcial1 & parcial2)
print("Aprobaron solo uno:", parcial1 ^ parcial2)
print("Aprobaron al menos uno:", parcial1 | parcial2)

# 8) Control de stock
stock = {}
producto = input("Ingresá el nombre de un producto para consultar o agregar: ")
if producto in stock:
    agregar = int(input("¿Cuántas unidades agregar?: "))
    stock[producto] += agregar
else:
    unidades = int(input("Producto no encontrado. Ingresá unidades para agregarlo: "))
    stock[producto] = unidades
print("Stock actualizado:", stock)

# 9) Agenda con tuplas
agenda_eventos = {
    ('lunes', '10:00'): 'Reunión',
    ('martes', '14:00'): 'Clase de programación',
}
dia = input("Ingresá el día para consultar: ")
hora = input("Ingresá la hora para consultar: ")
evento = agenda_eventos.get((dia, hora), "No hay evento programado.")
print(f"Evento en {dia} a las {hora}: {evento}")

# 10) Invertir diccionario de países y capitales
paises = {'Argentina': 'Buenos Aires', 'Francia': 'París', 'Italia': 'Roma'}
capitales = {capital: pais for pais, capital in paises.items()}
print("Diccionario invertido (capitales como claves):", capitales)
