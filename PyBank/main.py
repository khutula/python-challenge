from datetime import datetime
import os
import csv

dates = []
profits_losses = []

csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath, newline="",encoding = 'utf-8'):
    csvreader = csv.reader(csvfile,delimiter=",")
    for row in csvreader:
        dates.append(row[0])
        profits_losses.append(row[1])