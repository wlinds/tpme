import csv
import numpy as np

def gen_address():
    street_names = []
    with open('Data/datasets/ssn.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            street_names.append(row['Street Name'])

    return np.random.choice(street_names) + " " + str(np.random.randint(1,30))

def gen_postal():
    first_part = np.random.randint(100, 999)
    second_part = np.random.randint(10, 99)
    postal_code = f"{first_part} {second_part}"
    return postal_code

def gen_country():
    return 'Sweden'

def gen_city():
    return np.random.choice(['Göteborg', 'Stockholm', 'Malmö'])
    

if __name__ == "__main__":
    print(gen_address())