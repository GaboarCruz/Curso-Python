import csv 


with open('21.csvfiles/monthly_sales.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    fieldnames = csv_reader.fieldnames + ['sales + sales']

    with open('21.csvfiles/updated_monthly_sales.csv', 'w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        for row in csv_reader:
            row['sales + sales'] = int(row['sales']) + int(row['sales'])
            csv_writer.writerow(row)
        