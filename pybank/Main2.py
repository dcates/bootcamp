# -*- coding: UTF-8 -*-
"""Average Numbers."""


def average(numbers):
    """Calculate the average for a list of numbers.

    Args:
        numbers (list): A list of integers.

    Return:
        The average value for a list of numbers.

    """
    length = len(numbers)
    sum = 0.0
    for number in numbers:
        sum += number
    return sum / length


def main():
    """main function."""
    #print(average([1, 5, 9]))
    #print(average(range(11)))
# -*- coding: UTF-8 -*-
"""Employee Email Script.

This module allows us to create an email address using employee data from
a csv file.

Example:
    $ python employee_email.py

"""
import os
import csv

filepath = os.path.join("budget_data_1.csv")

date = []

# Read data into dictionary and create a new email field
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        date = row["Date"]
        revenue = row["Revenue"]
        #email = f"{first_name}.{last_name}@example.com"
        #new_employee_data.append({"date": row["date"],"revenue": row["revenue"]})

# Grab the filename from the original path
##_, filename = os.path.split(filepath)

# Write updated data to csv file
##csvpath = os.path.join("test.csv")
##with open(csvpath, "w") as csvfile:
##    csvwriter = csv.writer(csvfile, delimiter= ',')
##    fieldnames = ["revenue", "date"]
    #csvwriter .writerow(["date"])
    #csvwriter .writerow(["revenue"])
 ##   fieldnames = ["date"]
   ## fieldnames = ["revenue"]
    ##writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    ##writer.writeheader()

##print(fieldnames)
#######################
#print(sum(int(revenue)))
for rev in revenue:
	print(revenue)

for index, rev in enumerate(revenue):
    rev=revenue[index]
if __name__ == "__main__":
    main()

