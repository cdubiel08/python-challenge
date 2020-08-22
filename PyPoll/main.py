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

    #total votes = to length of list as each line is a vote
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
        percentVote = votes[i]/totalVotes * 100
        print(f"{uniqueNames[i]}: {percentVote:.3f}% ({votes[i]})")

    #find winner
    winnerIndex = votes.index(max(votes)) #returns index value for largest integer in list
    winner = uniqueNames[winnerIndex]

    print("-------------------------------------")
    print(f"Winner: {winner}")
    print("-------------------------------------")    


    output_path = os.path.join("analysis","output.txt")
    with open(output_path, 'w') as textfile:
        textfile.write("Election Results\n")
        textfile.write("--------------------------------\n")
        textfile.write(f"Total Votes: {totalVotes}\n")
        
        for i in range(len(uniqueNames)):
            percentVote = votes[i]/totalVotes * 100
            textfile.write(f"{uniqueNames[i]}: {percentVote:.3f}% ({votes[i]})\n")
        
        textfile.write(f"-------------------------------------\n")
        textfile.write(f"Winner: {winner}\n")
        textfile.write(f"-------------------------------------\n")