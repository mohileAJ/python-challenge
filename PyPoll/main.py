# Dependencies / Modules
import os
import csv

# Lists to store data
votes_cast = []
ballot_id_count = []
Voter_ID_count = [0, 0, 0]
Candidates_with_votes = []

# Counters
vote_count = 0
max_votes = 0

# Set path for the input file, 'election_data.csv' 
input_path = os.path.join('Resources', 'election_data.csv')

# Open, and read in, the input file; 
with open(input_path, 'r') as input_file:
    csv_reader = csv.reader(input_file, delimiter = ',')
    csv_header = next(csv_reader)

    print("Election Results\n--------------------")

# Loop through looking for total number of Ballot IDs
    for votes_data in csv_reader:
        if(type((votes_data)[0]) == str) and (type((votes_data)[1]) == str) and (type((votes_data)[2]) == str) and (len((votes_data)[0]) != 0) and (len((votes_data)[1]) != 0) and (len((votes_data)[2]) != 0):
            votes_cast.append((((votes_data)[0]), ((votes_data)[2])))
    # print(len(votes_cast)) 
    print(f"Total Votes: {len(votes_cast)}")
    print("--------------------")
            
# Loop through looking for candidates' (unique name occurrence for each candidate)       
    for candidate in votes_cast:
        if candidate[1] not in Candidates_with_votes:
            Candidates_with_votes.append(candidate[1])
    # print(Candidates_with_votes)
    # print(len(Candidates_with_votes))

    for i in votes_cast:
        for x_idx in range(len(Candidates_with_votes)):
            if i[1] == Candidates_with_votes[x_idx]:
                Voter_ID_count[x_idx] += 1

# Loop through the full candidates_with_votes list
    for x_index in range(len(Candidates_with_votes)):
        vote_count = str(Voter_ID_count[x_index])
        candidate_name = str(Candidates_with_votes[x_index])     
        print(f"{candidate_name}: {((int(vote_count)/int(len(votes_cast))) * 100):.3f}% ({vote_count})")   
    
    for index, candidate in enumerate(Voter_ID_count):
        if Voter_ID_count[index] > Voter_ID_count[max_votes]:
            max_votes = index
    
    print("--------------------")
    print(f"Winner: {Candidates_with_votes[max_votes]}")
    print("--------------------")

# Set path for the output file, 'results.txt')
output_path = os.path.join("analysis", "results.txt")

# Open the output file using "write" mode.  Hold the contents in a variable, results_file: create a header row and oyjer content for Analysis
with open(output_path, 'w') as results_file:
  
# Create the first two row for a Table header        
    print('Election Results\n--------------------', file=results_file)
    print(f"Total Votes: {len(votes_cast)}\n--------------------", file=results_file)
    for x_index in range(len(Candidates_with_votes)):
        vote_count = str(Voter_ID_count[x_index])
        candidate_name = str(Candidates_with_votes[x_index])    
        print(f"{candidate_name}: {((int(vote_count)/int(len(votes_cast))) * 100):.3f}% ({vote_count})", file=results_file)
    print('--------------------', file=results_file)
    print(f"Winner: {Candidates_with_votes[max_votes]}", file=results_file)
    print('--------------------', file=results_file)