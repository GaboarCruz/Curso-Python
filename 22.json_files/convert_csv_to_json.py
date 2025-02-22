import csv
import json

# Cargamos la ruta de el archivo csv
csv_file_path = '22.json_files/products.csv'
data = []

# Abrimos el archivo csv para lectura
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        data.append(row)
        
# Creamos Ruta del archivo JSON
json_file_path = '22.json_files/new_products.json'

# Abrimos y cargamos el archivo JSON
with open(json_file_path, 'w')as json_file:
    # Convertimos la lista de diccionario a JSON
    json.dump(data, json_file, indent=4)
