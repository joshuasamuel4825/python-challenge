#import dependencies
import csv
from ctypes import cast
import os

#declare variables

candidate =[]
diana_votes = 0
raymon_votes =0
caspar_votes=0
total = 0
#set path to csv
path = os.path.join('Resources','election_data.csv')
output_path = os.path.join('analysis','output.txt')
#loop through file
with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
#remove header
    csvheader = next(csvreader)
    #create list just for candidates
    for line in csvreader:
        
        candidate.append(line[2])
    #find total number of votes
    total = len(candidate)
    #find total votes for each candidate
    for line in candidate:
        if line == "Diana DeGette":
            diana_votes+=1
        elif line == "Raymon Anthony Doane":
            raymon_votes+=1
        elif line == "Charles Casper Stockham":
            caspar_votes+=1
    #determine winner from votes
    if diana_votes> raymon_votes & caspar_votes:
        winner = "Diana DeGette"
    elif raymon_votes>caspar_votes&diana_votes:
        winner="Raymon Anthony Doane"
    elif caspar_votes> diana_votes&raymon_votes:
        winner= "Charles Caspar Stockham"
    #Print Statements
    print("Election Results")
    print("----------------------------")
    print(" ")
    print(f"Total Votes: {total}")
    print(" ")
    print('----------------------------')
    print(f"Charles Caspar Stockham:  {'{:.3f}'.format((caspar_votes/total)*100)}% ({caspar_votes}) ")
    print(f"Diana DeGette:  {'{:.3f}'.format((diana_votes/total)*100)}% ({diana_votes}) ")
    print(f"Raymon Anthony Doane:  {'{:.3f}'.format((raymon_votes/total)*100)}% ({raymon_votes}) ")
    print("---------------------------------")
    print(f'Winner: {winner}')
    
#Print to text file
with open(output_path, 'w') as file:
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write(" \n")
    file.write(f"Total Votes: {total}")
    file.write(" \n")
    file.write('----------------------------\n')
    file.write(f"Charles Caspar Stockham:  {'{:.3f}'.format((caspar_votes/total)*100)}% ({caspar_votes}) \n")
    file.write(f"Diana DeGette:  {'{:.3f}'.format((diana_votes/total)*100)}% ({diana_votes}) \n")
    file.write(f"Raymon Anthony Doane:  {'{:.3f}'.format((raymon_votes/total)*100)}% ({raymon_votes}) \n")
    file.write("---------------------------------\n")
    file.write(f'Winner: {winner}')