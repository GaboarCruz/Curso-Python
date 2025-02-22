import os

# Obtener el directorio actual
'''
cwd = os.getcwd()
print("Directorio Actual", cwd)
'''

# Listar los archivos .txt
txt_files = [f for f in os.listdir('./23.os_math_random.py') if f.endswith('.txt')]
print(txt_files)

# Renombrar archivos
os.rename('caperucita.txt', 'cuento.txt')
print("Archivo renombrado")

# Listar los archivos .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print(txt_files)

