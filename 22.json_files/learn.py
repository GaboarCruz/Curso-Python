import json

new_product = {
    'name': 'Wireless Charger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry': '2024-07-01'
}

file_path = '22.json_files/products.json'

with open(file_path, 'r') as file:
    products = json.load(file)

products.append(new_product)

with open(file_path, 'w') as file:
    json.dump(products, file, indent=4)
