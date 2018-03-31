
import os
import csv

reader = csv.DictReader(open("budget_data_1.csv"))

pybank_dict = []

# Read data into dictionary and create a new email field
for line in reader:
    pybank_dict.append(line)
print(pybank_dict)
#print(line)

#rev_nums = [rev for rev in pybank_dict]
#print(rev_nums)

#count = {}
#for element in pybank_dict:
#    count[element] = count.get(element, 0) + 1
#print(count)