from datetime import datetime
import os
import csv

dates = []
profits_losses = []
net_total = 0
changes = []
total_change = 0
max_increase = 0
max_decrease = 0

csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath, newline="",encoding = 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    for row in csvreader:
        dates.append(row[0])
        profits_losses.append(row[1])

for i in range(1,len(profits_losses)):
    net_total += int(profits_losses[i])
    if i > 1:
        changes.append(int(profits_losses[i])-int(profits_losses[i-1]))

for index, change in enumerate(changes):
    total_change += change
    if change > max_increase:
        max_increase = change
        max_inc_month = dates[index + 2]
    elif change < max_decrease:
        max_decrease = change
        max_dec_month = dates[index + 2]

average_change = round(total_change / len(changes), 2)

lines = []

lines.append("Financial Analysis")
lines.append("-----------------------------")
lines.append( "Total Months: " + str(len(dates)-1))
lines.append("Total: $" + str(net_total))
lines.append("Average Change: $" + str(average_change))
lines.append("Greatest Increase in Profits: " + max_inc_month + " ($" + str(max_increase) + ")")
lines.append("Greatest Decrease in Profits: " + max_dec_month + " ($" + str(max_decrease) + ")")

output_path = os.path.join("Analysis","pybank_results.txt")

with open(output_path, "w", newline = "") as txtfile:
    for line in lines:
        txtfile.writelines([line+"\n"])
        print(line)