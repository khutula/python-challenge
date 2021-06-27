# import modules
import os
import csv

# set lists for reading in data
dates = []
profits_losses = []

# create path for csv file to be read
csvpath = os.path.join("Resources","budget_data.csv")

# open csv file and read through
with open(csvpath, newline="",encoding = 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    # skip header row
    header = next(csvreader)

    # each row is looped through: months are added to dates list & net profit/loss is added to profits_loss list
    for row in csvreader:
        dates.append(row[0])
        profits_losses.append(row[1])

# set variable for tracking net total profits/losses
net_total = 0

# set list for recording net change from month to month
changes = []

# loop through every entry in the profits_losses list & add it to the net_total
for i in range(len(profits_losses)):
    net_total += int(profits_losses[i])

    # calcualte net change from month (i) to month (i - 1) only if we aren't looking at the first month's data
    if i > 0:
        changes.append(int(profits_losses[i])-int(profits_losses[i-1]))

# set variable for calculating total net change
total_change = 0

# set variables for recording max increase & max decrease in profits values
max_increase = 0
max_decrease = 0

# loop through each net change in the changes list to calculate total net change & max values
for index, change in enumerate(changes):

    # calcuate total net change - to be used in average_change
    total_change += change

    # if the change value a max increase or max decrease in profits, assign value & month to respective variables
    if change > max_increase:
        max_increase = change
        max_inc_month = dates[index + 1]
    elif change < max_decrease:
        max_decrease = change
        max_dec_month = dates[index + 1]

# calculate the average monthly change
average_change = round(total_change / len(changes), 2)

# set list for capturing all lines to be printed
lines = []

# add strings to each item of the lines list
lines.append("Financial Analysis")
lines.append("-----------------------------")
lines.append( "Total Months: " + str(len(dates)))
lines.append("Total: $" + str(net_total))
lines.append("Average Change: $" + str(average_change))
lines.append("Greatest Increase in Profits: " + max_inc_month + " ($" + str(max_increase) + ")")
lines.append("Greatest Decrease in Profits: " + max_dec_month + " ($" + str(max_decrease) + ")")

# create the output text file
output_path = os.path.join("Analysis","pybank_results.txt")

# write to the outpuut text file the results
with open(output_path, "w", newline = "") as txtfile:

    # loop through all lines and print to both the text file and the terminal
    for line in lines:
        txtfile.writelines([line+"\n"])
        print(line)