# Leer un archivo linea por linea
""""
with open('20.text_management.py/caperucita.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())
"""

# Leer todas las lineas en una lista
"""
with open('20.text_management.py/caperucita.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
"""

# Añadir Texto
"""
with open('20.text_management.py/caperucita.txt', 'a') as file:
    file.write("\n\nEsto fue escrito por Chet Gipitee")
"""

# Sobreescribir Texto
"""
with open('20.text_management.py/caperucita.txt', 'w') as file:
    file.write("\n\nBy chet yipiti")
"""

# Mandar el total de lineas
with open('20.text_management.py/caperucita.txt', 'r') as file:
    lines = file.readlines()
    print(len(lines))