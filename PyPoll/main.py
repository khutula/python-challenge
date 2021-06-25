import os
import csv

vote_count = 0
candidates = {}

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath, newline="",encoding = 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    for row in csvreader:
        if candidates.get(row[2], False):
            candidates[row[2]] += 1
        elif row[2] != "Candidate": 
            candidates[row[2]] = 1