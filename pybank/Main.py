# -*- coding: UTF-8 -*-
"""Employee Email Script.

This module allows us to create an email address using employee data from
a csv file.

Example:
    $ python employee_email.py

"""
import os
import csv

filepath = os.path.join("budget_data_2.csv")

budget_data = []

# Read data into dictionary and create a new email field
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        date1 = row["Date"]
        revenue = row["Revenue"]
        email = f"{date1}.{revenue}@example.com"
        #new_employee_data.append({"date": row["date"],"revenue": row["revenue"]})
        budget_data.append(
            {
                "Date": row["Date"],
                "Revenue": row["Revenue"]
                #"email": email
            })
print(budget_data)
