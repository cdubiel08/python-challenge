import os
import csv
import statistics

csvpath = os.path.join('Resources', 'Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')


with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    budgetList = []
    profitLossSubset = []
    maxMonth = ""
    minMonth = ""
    for row in csvreader:
        budgetList.append(row)
        profitLossSubset.append(int(row[1]))

    noMonths = len(budgetList)
    totalNet = sum(profitLossSubset)
    averageMonthlyProfit = sum(profitLossSubset)/len(budgetList)
    maxProfit = max(profitLossSubset)
    minProfit = min(profitLossSubset)

    for row in budgetList:
        if int(row[1]) == max(profitLossSubset):
            maxMonth = row[0]
        if int(row[1]) == min(profitLossSubset):
            minMonth = row[0]

    print("Financial Analysis")
    print("--------------------------------")
    print(f"Total Months: {noMonths}")
    print(f"Total: {totalNet}")
    print(f"Average Change: ${averageMonthlyProfit}")
    print(f"Greatest Increase in Profits: {maxMonth} (${maxProfit})")
    print(f"Greatest Decrease in Profits: {minMonth} (${minProfit})")

    output_path = os.path.join("new.txt")
    with open(output_path, 'w') as textfile:
        textfile.write("Financial Analysis\n")
        textfile.write("--------------------------------\n")
        textfile.write(f"Total Months: {noMonths}\n")
        textfile.write(f"Total: {totalNet}\n")
        textfile.write(f"Average Change: ${averageMonthlyProfit}\n")
        textfile.write(f"Greatest Increase in Profits: {maxMonth} (${maxProfit})\n")
        textfile.write(f"Greatest Decrease in Profits: {minMonth} (${minProfit})\n")
        