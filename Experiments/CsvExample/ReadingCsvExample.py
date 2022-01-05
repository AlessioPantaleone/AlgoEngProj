import csv
import pandas as pd


filename = 'Read.csv'
f = open(filename, 'r')

with f:
    reader = csv.reader(f)
    print("PRINTING FROM CSV READER:")
    for row in reader:
        print(row)

data = pd.read_csv(filename)
print("\nPRINTING FROM PANDAS:")
print(data)



