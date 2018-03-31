import csv
import os

# Set path for file
# csvpath = os.path.join("Resources", "netflix_ratings.csv")

output_path = os.path.join('files', 'ssn.csv')
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter= ',')
    csvwriter .writerow(['first name', 'last', 'ssn'])
    csvwriter .writerow(['darr', 'cates', '654'])
    csvwriter .writerow(['123', 'cates', '654'])
    csvwriter .writerow(['Sarah', 'Francis', '8675309'])