import os
import csv

csvpath = os.path.join('Resources', 'Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')


with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
        
    # get list of unique names
    candidatesNamedSubset = []
    for row in csvreader:
        candidatesNamedSubset.append(row[2])
    
    uniqueNames = list(set(candidatesNamedSubset))

    #total votes = to length of list as each line is a
    totalVotes = len(candidatesNamedSubset)

    # initialize votes list with 0s = to number of candidates
    votes = []
    for i in range(len(uniqueNames)):
        votes.append(0)

     # reset file to re-iterate
    csvfile.seek(0)
    csvreader2 = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader2)
    
    # count votes for each candidate
    for row in csvreader:        
        for i in range(len(uniqueNames)):
            if row[2] == uniqueNames[i]:
                votes[i] = votes[i] + 1

    # print results
    print("Election Results")
    print("-------------------------------------")
    print(f"Total Votes: {totalVotes}")

    for i in range(len(uniqueNames)):
        percentVote = votes[i]/totalVotes
        print(f"{uniqueNames[i]}: {percentVote}% ({votes[i]})")

    #find winner
    winnerIndex = votes.index(max(votes)) #returns index value for largest integer in list
    winner = uniqueNames[winnerIndex]

    print("-------------------------------------")
    print(f"Winner: {winner}")
    print("-------------------------------------")    


    # # profitLossSubset = []
    # # maxMonth = ""
    # # minMonth = ""
    # # for row in csvreader:
    # #     budgetList.append(row)
    # #     profitLossSubset.append(int(row[1]))

    # # noMonths = len(budgetList)
    # # totalNet = sum(profitLossSubset)
    # # averageMonthlyProfit = sum(profitLossSubset)/len(budgetList)
    # # maxProfit = max(profitLossSubset)
    # # minProfit = min(profitLossSubset)

    # # for row in budgetList:
    # #     if int(row[1]) == max(profitLossSubset):
    # #         maxMonth = row[0]
    # #     if int(row[1]) == min(profitLossSubset):
    # #         minMonth = row[0]

    # # print("Financial Analysis")
    # # print("--------------------------------")
    # # print(f"Total Months: {noMonths}")
    # # print(f"Total: {totalNet}")
    # # print(f"Average Change: ${averageMonthlyProfit}")
    # # print(f"Greatest Increase in Profits: {maxMonth} (${maxProfit})")
    # # print(f"Greatest Decrease in Profits: {minMonth} (${minProfit})")

    # # output_path = os.path.join("analysis","output.txt")
    # # with open(output_path, 'w') as textfile:
    # #     textfile.write("Financial Analysis\n")
    # #     textfile.write("--------------------------------\n")
    # #     textfile.write(f"Total Months: {noMonths}\n")
    # #     textfile.write(f"Total: {totalNet}\n")
    # #     textfile.write(f"Average Change: ${averageMonthlyProfit}\n")
    # #     textfile.write(f"Greatest Increase in Profits: {maxMonth} (${maxProfit})\n")
    # #     textfile.write(f"Greatest Decrease in Profits: {minMonth} (${minProfit})\n")