import csv

# Leer un archivo
'''
with open('21.csvfiles/products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)
'''

# Mostrar info por columnas
'''
with open('21.csvfiles/products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto: {row['name']}, Precio {row['price']}")
'''

new_product = {
    'name': 'Wireless Charger',
    'price': 75,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry': '2024-07-01'
}

with open("21.csvfiles/products.csv", mode='a', newline='') as file:
    file.write('\n')
    csv_writer = csv.DictWriter(file, fieldnames= new_product.keys())
    csv_writer.writerow(new_product)