# read_csv.py
import csv

filename = 'C:\\temp\\finance_header.csv'
# with open(filename) as f:
#     print(type(f))
#     reader = csv.reader(f)
#     print(type(reader))
#     data = list(reader)
#     print(type(data))

# print(data)

# Use csv.reader()
file = open(filename)
csvreader = csv.reader(file)

# Extract field names.
header = []
header = next(csvreader)
print("Header: ", header)

# Extract the rows.
print("The rows...")
rows = []
for row in csvreader:
    rows.append(row)
    print(row)
print("All rows...")
print(rows)

file.close()
