import os
csvpath = os.path.join("budget_data_1.csv")
import csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    for row in csvreader:
        print(row)
b = sum row
print(b)
