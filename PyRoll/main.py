import csv
from collections import Counter
import os
electionData = os.path.join('election_data.csv')


with open(electionData, 'r', newline='', encoding='latin-1') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader) 

    votesCount = Counter() 
    candList = [] 
    percentage = [] 
    answer = [] 

    for row in csvreader: 
        candList.append(row[2])

    totalVotes = len(candList)

    for name in candList: 
        votesCount[name] += 1

    winner = max(zip(votesCount.values(), votesCount.keys())) 
    names = tuple(votesCount.keys())
    votes = tuple(votesCount.values())

    for x in votes:
        percentage.append((int(x)/totalVotes)*100) 
    
    answer.append('Election Results')
    answer.append('-----------------------')
    answer.append('Total Votes: ' + str(totalVotes))
    answer.append('-----------------------')
    for x in range(len(names)):
        answer.append(names[x] + ': ' + str(round(percentage[x],1)) + '% ' + '(' + str(votes[x]) + ')')
    answer.append('-----------------------')
    answer.append('Winner: ' + winner[1])
    answer.append('-----------------------')

    print("\n".join((answer)))