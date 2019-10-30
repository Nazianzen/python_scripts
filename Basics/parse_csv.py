import csv

with open('temp.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        field_names = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnames=field_names, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
