import csv
import re

with open(r"C:\Users\PC\Downloads\Crimes.csv") as file_csv:
    reader = csv.DictReader(file_csv)
    types = {}
    for row in reader:
        if re.match(r"\d\d/\d\d/2015.*", row['Date']):
            if row['Primary Type'] in types:
                types[row['Primary Type']] += 1
            else:
                types[row['Primary Type']] = 1
    print(sorted(types , key=lambda x: types[x]), sep='\n')