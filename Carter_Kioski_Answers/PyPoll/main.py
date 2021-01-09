import csv

read_path = 'Resources/election_data.csv'
write_path = 'analysis/analysis.txt'
winner = ''
vote_count = 0
votes = {}
with open(read_path) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    next(csvreader)
    for row in csvreader:
        vote_count += 1
        if row[2] not in votes.keys():
            votes[row[2]] = 1
        else:
            votes[row[2]] += 1


output1 = f'''Election Results
-------------------------
Total Votes: {vote_count}
-------------------------'''
print(output1)
#prints the vote count for each person
for k,v in votes.items():
    if votes[k] == max(votes.values()):
        winner = k
    print(f'{k}: {round(v/vote_count*100,2)} ({v})')

output2 = f'''-------------------------
Winner: {winner}
-------------------------'''
print(output2)
#writes output to the analysis.txt file 
with open(write_path, 'w') as file:
    file.write(output1)        
    file.write('\n')
    for k,v in votes.items():
        file.write(f'{k}: {round(v/vote_count*100,2)} ({v})')
        file.write('\n')
    file.write(output2)