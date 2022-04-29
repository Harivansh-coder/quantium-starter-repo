import csv

csv_files = ['daily_sales_data_0', 'daily_sales_data_1', 'daily_sales_data_2']
fieldnames = ['sales', 'date', 'region']

with open('quantium-starter-repo/data/processed_sales_data.csv', mode='w',newline="") as processed_csv_file:
    writer = csv.DictWriter(processed_csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for file_name in csv_files:
        with open(f'quantium-starter-repo/data/{file_name}.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if (row["product"] == "pink morsel"):
                    writer.writerow({"sales":float(row["price"][1:]) * float(row["quantity"]), "date":row["date"], "region":row["region"]})
                
                    

            