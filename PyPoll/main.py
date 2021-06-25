import os
import csv

vote_count = 0
candidates = {}
vote_percent = 0
highest_votes = 0
print_lines = []

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
    if votes > highest_votes:
        winner = candidate
        highest_votes = votes

print_lines.append("Election Results")
print_lines.append("-----------------------------")
print_lines.append("Total Votes: " + str(vote_count))
print_lines.append("-----------------------------")

for candidate, votes in candidates.items():
    vote_percent = round(votes/vote_count*100,3)
    print_lines.append(candidate + ": " + str(vote_percent) + "% (" + str(votes) + ")")

print_lines.append("-----------------------------")
print_lines.append("Winner: " + winner)
print_lines.append("-----------------------------")

output_path = os.path.join("Analysis","pypoll_results.txt")

with open(output_path, "w") as txtfile:       
    for line in print_lines:
        txtfile.writelines([line+"\n"])
        print(line)