
# -*- coding: UTF-8 -*-
"""Employee Email Script.

This module allows us to create an email address using employee data from
a csv file.
Example:
    $ python employee_email.py
"""
import os
import csv
filepath = os.path.join("raw_data","election_data_1.csv")
election_data = []
my_list = []
my_dict = {}
my_counter = 0
my_string = ""
# Read data into dictionary and create a new email field
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        voter_id = row["Voter ID"]
        county = row["County"]
        candidate = row["Candidate"]
        #email = f"{first_name}.{last_name}@example.com"
        election_data.append(
            {
                "voter_id": row["Voter ID"],
                "county": row["County"],
                "candidate": row["Candidate"],
                #"email": email
            }
        )
# Grab the filename from the original path
_, filename = os.path.split(filepath)
print("Election Results")
print("-" * 50)
print ("Total Votes : %d" % len(election_data))
print("-" * 50)

# Iterate through a list
#zoo = ["cow", "dog", "bee", "zebra"]
#for can in candidate:
#  print(can) 

#print("----------------------------------------")
#d=election_data
#b=[j[0] for i in d for j in i.items()]
#for k in list(set(b)):
#    print("{0}: {1}".format(k,b.count(k)))


#for key in election_data:
#    print (key, election_data[key])
#--------------------------------------------
for word in election_data:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 
for words in frequency_list:
    print (words, frequency[words])