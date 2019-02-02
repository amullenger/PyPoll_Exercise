import os
import csv

election_data_path = os.path.join('', 'election_data.csv')

master_list = []
total_votes = 0
num_khan_votes = 0
num_correy_votes = 0
num_li_votes = 0
num_otooley_votes = 0
results = []
winner = ''


with open(election_data_path, 'r', newline='') as csvfile:
    election_data_reader = csv.reader(csvfile)
    next(election_data_reader)

    for row in election_data_reader:
        master_list.append([float(row[0]), row[1], row[2]])
for i in range(5):
    print(master_list[i])
total_votes=len(master_list)
print(total_votes)

for i in range(len(master_list)):
    if master_list[i][2] == 'Khan':
        num_khan_votes += 1
    if master_list[i][2] == 'Correy':
        num_correy_votes += 1
    if master_list[i][2] == 'Li':
        num_li_votes += 1
    if master_list[i][2] == "O'Tooley":
        num_otooley_votes += 1

results_tracker = 0
results = [['Khan', num_khan_votes], ['Correy', num_correy_votes], ['Li', num_li_votes], ["O'Tooley", num_otooley_votes]]
for i in range(len(results)):
    if results[i][1] > results_tracker:
        results_tracker = results[i][1]
        winner = results[i][0]

print(num_khan_votes)

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