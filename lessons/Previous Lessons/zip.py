import csv
import os

csvpath = os.path.join('files', 'WebDevelopment.csv')

with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delmiiter=',')

	print(csvreader)
	for row in csvreader:
		print(row)
