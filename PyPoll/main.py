# Dependencies / Modules
import os
import csv

# Lists to store data
votes_cast = []
Candidates_with_votes = []
Voter_ID_count = [0, 0, 0]
# ballot_id_count = []

# Counters
vote_count = 0
max_votes = 0

# Set path for the input file, 'election_data.csv' 
input_path = os.path.join('Resources', 'election_data.csv')

# Open, and read in, the input file; and split the 'str' datatype data on commas 
with open(input_path, 'r') as input_file:
    csv_reader = csv.reader(input_file, delimiter = ',')
  
  # Store the header row
    csv_header = next(csv_reader)

    print("Election Results\n--------------------")

# Loop through looking for total number of Ballot IDs, and append the valid votes to an array -- votes_cast[]
    for votes_data in csv_reader:
        if(type((votes_data)[0]) == str) and (type((votes_data)[1]) == str) and (type((votes_data)[2]) == str) and (len((votes_data)[0]) != 0) and (len((votes_data)[1]) != 0) and (len((votes_data)[2]) != 0):
            votes_cast.append((((votes_data)[0]), ((votes_data)[2])))
    print(f"Total Votes: {len(votes_cast)}")
    print("--------------------")

# Loop through looking for ballot IDs (unique Ballot ID occurrence for the votes casted)       
    # for ballot_id in votes_cast:
    #     if ballot_id[0] not in ballot_id_count:
    #         ballot_id_count.append(ballot_id[0])  
    # print(len(ballot_id_count))

# Loop through looking for candidates' (unique name occurrence for each candidate)       
    for candidate in votes_cast:
        if candidate[1] not in Candidates_with_votes:
            Candidates_with_votes.append(candidate[1])

# Loop through the full Candidates_with_votes[] and finding / matching each listed candidate's indices with that of the candidate's respective index in the Voter_ID_count[] array and adding their vote to such index' 
    for candidate_vote in votes_cast:
        for candidate_idx in range(len(Candidates_with_votes)):
            if candidate_vote[1] == Candidates_with_votes[candidate_idx]:
                Voter_ID_count[candidate_idx] += 1

# Loop through the full Candidates_with_votes[]; Gather the count of each candidates' votes and print them alongside the candidates' names
    for candidate_idx in range(len(Candidates_with_votes)):
        vote_count = str(Voter_ID_count[candidate_idx])
        candidate_name = str(Candidates_with_votes[candidate_idx])     
        print(f"{candidate_name}: {((int(vote_count)/int(len(votes_cast))) * 100):.3f}% ({vote_count})")   
    
# Loop through the Voter_ID_count[] to find max votes' count [index]    
    for index, candidate in enumerate(Voter_ID_count):
        if Voter_ID_count[index] >= Voter_ID_count[max_votes]:
            max_votes = index
    
    print("--------------------")
    print(f"Winner: {Candidates_with_votes[max_votes]}")
    print("--------------------")

# Set path for the output file, 'results.txt')
output_path = os.path.join("analysis", "results.txt")

# Open the output file using "write" mode.  Hold the contents in a variable, results_file: create a header row and other content for Analysis
with open(output_path, 'w') as results_file:
  
# Create the first two row for a Table header        
    print('Election Results\n--------------------', file=results_file)
    print(f"Total Votes: {len(votes_cast)}\n--------------------", file=results_file)
    for candidate_idx in range(len(Candidates_with_votes)):
        vote_count = str(Voter_ID_count[candidate_idx])
        candidate_name = str(Candidates_with_votes[candidate_idx])    
        print(f"{candidate_name}: {((int(vote_count)/int(len(votes_cast))) * 100):.3f}% ({vote_count})", file=results_file)
    print('--------------------', file=results_file)
    print(f"Winner: {Candidates_with_votes[max_votes]}", file=results_file)
    print('--------------------', file=results_file)