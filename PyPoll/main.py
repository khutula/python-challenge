import os
import csv

vote_count = 0
candidates = {}
vote_percent = []

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath, newline="",encoding = 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    for row in csvreader:
        if candidates.get(row[2], False):
            candidates[row[2]] += 1
        elif row[2] != "Candidate": 
            candidates[row[2]] = 1

for candidate, votes in candidates.items():
    vote_count += votes

for candidate, votes in candidates.items():
    vote_percent.append(round(votes/vote_count*100,3))