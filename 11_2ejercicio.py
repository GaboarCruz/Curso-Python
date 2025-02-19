# 1. Doble de los numeros
numeros = [1,2,3,4,5]
nuevaLista = [x**2 for x in numeros]
print(nuevaLista) #[1, 4, 9, 16, 25]

# 2. Filtrar y Transformar en un Solo Paso
palabras = ["sol", "mar", "montaña", "rio", "estrella"]
nuevaLista = [word.upper() for word in palabras if len(word) > 3]
print(nuevaLista) #['MONTAÑA', 'ESTRELLA']

# 3. Crear un Diccionario con List Comprehension
claves = ["nombre", "edad", "ocupación"]
valores = ["Juan", 30, "Ingeniero"]
nuevoDiccionario = {claves[i]: valores[i] for i in range(len(claves))}
print(nuevoDiccionario) # {'nombre': 'Juan', 'edad': 30, 'ocupación': 'Ingeniero'}

# 4. Anidación de List Comprehensions
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
nuevaMatriz = [[row[i] for row in matriz]for i in range(len(matriz[0]))]
print(nuevaMatriz) # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# 5.Extraer Información de una Lista de Diccionarios0
personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]
informacion = [persona for persona in personas if persona['ciudad'] == "Madrid" and persona["edad"] > 30] 
print(informacion) 
#[{'nombre': 'Ana', 'edad': 32, 'ciudad': 'Madrid'}, {'nombre': 'Laura', 'edad': 40, 'ciudad': 'Madrid'}]

# 6.List Comprehension con un else
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nuevosNumeros = [numero * 2 if numero % 2 == 0 else numero for numero in numeros]
print(nuevosNumeros) #[1, 4, 3, 8, 5, 12, 7, 16, 9, 20]