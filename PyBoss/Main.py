
# -*- coding: UTF-8 -*-
"""clean up Employee Data Script.

This module allows us to clean up data for employee id, name, dob, ssn, and state information
"""
import os
import csv
from datetime import datetime

#state dictionary used for abbreviation lookups
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
#file to clean up
filepath = os.path.join("raw_data", "employee_data1.csv")
#to store data from csv
new_employee_data = []

# Read data into dictionary and create a fields for employee id, name, dob, ssn, and state
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #pulls employee id from csv and stores in list
        emp_id = row["Emp ID"]
        #pulls employee full name from csv and stores in list
        name = row["Name"]
        #pulls first name from full name and stores in list
        first_name = name.split()[0]
        #pulls last name from full name and stores in list
        last_name = name.split()[1]
        #pulls dob from csv and stores in list
        dob = row["DOB"]
        #pulls ssn from csv and stores in list
        ssn = row["SSN"]
        #splits ssn by - delimiter and puts 3rd item in list (or the last 4 digits in this case)
        ssn6 = ssn.split("-")[2]
        #adds in * to "mask" the beginning digits of ssn
        ssn7 = "***-**-"+ ssn6
        #defining s for format manip
        s = dob
        #pulling in string format of date
        f = "%Y-%m-%d"
        #defining datetime and formating
        datetime = datetime.strptime(s, f)
        #formatted day month year, per instructions even though example shows month day year
        dob2 = datetime.strftime("%d-%m-%Y")
        #pulls state name and stores in list
        state = row["State"]
        #pulls state abbreviation from dictionary by looking at state name
        state1 = us_state_abbrev.get(state)
        #appends records into dictionary
        new_employee_data.append(
            {
                #sets header and what list it will pull from 

                "Emp ID": row["Emp ID"],
                "DOB": dob2,
                "First Name": first_name,
                "Last Name": last_name,
                "SSN": ssn7,
                "NewState": state1
            }
        )

# Grab the filename from the original path
_, filename = os.path.split(filepath)

# Write updated data to csv file
csvpath = os.path.join("raw_data", "pyboss_homework.csv")
with open(csvpath, "w") as csvfile:
    fieldnames = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "NewState"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_employee_data)
