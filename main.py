import os
import csv
#setting up the file path
polling = os.path.join("election_data.csv")

total_votes = 0.00
candidates = {}

#this dictionary is going to be {candidate : votes}}


winner = ""
winner_percent = 0


with open(polling) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
  
    for row in csvreader:
        total_votes += 1
        vote = row[2]
        if vote in candidates:
            candidates[vote] += 1
        else:
            candidates[vote]= 1

print(f'Election Results')
print(f'--------------------')
print(f'Total Votes: {total_votes}')
print(f'--------------------')

for candidate in candidates:
    votes = candidates[candidate]
    percent = votes/total_votes


    print(f'{candidate}: {percent:.2%} ({votes})')


    if percent > winner_percent:
        winner = candidate
        winner_percent = percent

print(f'--------------------')
print(f'Winner: {winner}')
print(f'--------------------')