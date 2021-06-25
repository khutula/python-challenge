from datetime import datetime
import os
import csv

dates = []
profits_losses = []
net_total = 0

csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath, newline="",encoding = 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    for row in csvreader:
        dates.append(row[0])
        profits_losses.append(row[1])

for i in range(1,len(profits_losses)):
    net_total += int(profits_losses[i])