import json
import csv

# Abrimos y Cargamos el JSON
json_file_path = '22.json_files/products.json'

with open(json_file_path, 'r') as json_file:
    data = json.load(json_file) # Cargamos los datos JSON en un objeto python

# Abrimos un archivo CSV para escribir
csv_file_path = '22.json_files/products.csv'
with open(csv_file_path, 'w', newline='') as csv_file:
    # Creamos un CSV writer
    csv_writer = csv.writer(csv_file)

    # Escribimos los encabezados (las primeras keys en el objeto JSON)
    header = data[0].keys()
    csv_writer.writerow(header)

    # Escribir el resto de filas
    for item in data:
        csv_writer.writerow(item.values())