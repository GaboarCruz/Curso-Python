import statistics
import csv

# Leer los datos de ventas mensuales desde un archivo CSV
monthly_sales = {}
with open('24.statistics/monthly_sales.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print(sales)

# Hallar la media
mean_sales = statistics.mean(sales)
print(f"La media es: {mean_sales}")

# Hallar la mediana
mean_sales = statistics.median(sales)
print(f"La mediana es: {mean_sales}")

# Hallar la moda
mean_sales = statistics.mode(sales)
print(f"La moda es: {mean_sales}")

# Hallar la desviación estandar
stdev_sales = statistics.stdev(sales)
print(f"La desviación estandar es: {stdev_sales}")

# Hallar la varianza
variance = statistics.variance(sales)
print(f"La variancia es: {variance}")

# El maximo de ventas es:
max_sales = max(sales)
min_sales = min(sales)

range_sales = max_sales - min_sales
print(f"Rango de ventas: {range_sales}")