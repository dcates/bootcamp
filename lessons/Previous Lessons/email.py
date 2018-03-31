import csv
import os

emails = os.path.join("files", "employees.csv")

with open(emails, newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        print(row)

    output_path = os.path.join('files', 'newemail.csv')
#with open(output_path, 'w', newline='') as csvfile:

    #csvwriter .writerow({employees{"1"}})

  with open('newemail.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(someiterable)