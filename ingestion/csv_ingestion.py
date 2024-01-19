import csv

def load_csv_data(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]
    return data