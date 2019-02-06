import os
import csv

election_data_path = os.path.join('', 'election_data.csv')

"""Instantiate variables for storing all data in a master list, tracking total votes and 
individual vote counts, storing results, and calculating the winner"""

master_list = []
total_votes = 0
num_khan_votes = 0
num_correy_votes = 0
num_li_votes = 0
num_otooley_votes = 0
results = []
winner = ''

"""Open file, store data in reader object, and append each row to a master list so we can 
easily perform necessary operations. Using next(reader object) function will skip the header 
row so our master list only contains voting data"""

with open(election_data_path, 'r', newline='') as csvfile:
    election_data_reader = csv.reader(csvfile)
    next(election_data_reader)

    for row in election_data_reader:
        master_list.append([float(row[0]), row[1], row[2]])

#The total # of votes is simply the length of the master list

total_votes=len(master_list)

#Iterate through master list and update vote total variables 

for i in range(len(master_list)):
    if master_list[i][2] == 'Khan':
        num_khan_votes += 1
    if master_list[i][2] == 'Correy':
        num_correy_votes += 1
    if master_list[i][2] == 'Li':
        num_li_votes += 1
    if master_list[i][2] == "O'Tooley":
        num_otooley_votes += 1

#Determine winner by storing candidate name with highest # of votes

results_tracker = 0
results = [['Khan', num_khan_votes], ['Correy', num_correy_votes], ['Li', num_li_votes], ["O'Tooley", num_otooley_votes]]
for i in range(len(results)):
    if results[i][1] > results_tracker:
        results_tracker = results[i][1]
        winner = results[i][0]

#print results in desired format

print(f"""\
    Election Results
    -------------------------
    Total Votes: {total_votes}
    -------------------------
    Khan: {round((num_khan_votes/total_votes)*100, 5)}% ({num_khan_votes})
    Correy: {round((num_correy_votes/total_votes)*100, 5)}% ({num_correy_votes})
    Li: {round((num_li_votes/total_votes)*100, 5)}% ({num_li_votes})
    O'Tooley: {round((num_otooley_votes/total_votes)*100, 5)}% ({num_otooley_votes})
    -------------------------
    Winner: {winner}""")