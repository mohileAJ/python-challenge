I have created the two main.py script files to prepare the analysis of the budget_data.csv and election_data.csv datasets provided for the PyBank and PyPoll challenges respectively. 

Upon running the main.py scripts, an analysis for each of the challenges is both printed to the terminal as well as to a text file that has the results (and saved in the respective 'analysis' folders). 

PyBank: 
With reference to the budget_data.csv provided, for the first element i.e. the "Date" column, we need to extract information relating to the number of months.  As month was a part of the str "Date" element [0]), we had to split the "Date" element (i.e., dates[0] and append it to a separate months array / list. 

I have used the date_objects[] and the sort statement to ensure that the dataset is sorted by Date, since we would be calculating daily changes in Profit/Loss and, therefore, the dataset needs to be listed chronologically. 

The "Profit/Loss" column was provided as 'str' type, which would have to be converted to 'int', considering that arithmetic operations needed to be performed on the "Profit/Loss" column for calculating the total profits (net of profit and loss amounts in the monthly observations over the period) as well as for calculating the daily change in Profit/Loss amounts. 

PyPoll: 
The valid votes were determined by ensuring that all the rows and columns in the "election_data.csv" were not empty or missing information (lines 28 - 30).  

Additionally, I checked if any Ballot_ID was appearing more than once by running the statements on line 9 and lines 34 - 38 (these have been commented out as the array is very long and takes several minutes to run), which returned the same number of rows as the votes_cast[], indicating there were only unique values in votes_cast[0]. 

In order to avoid hard-coding the candidate names - 
    - created a list of candidates (i.e. Candidates_with_votes);  
    - used the indices of this list (along with counters) to find matching candidate names in the votes_cast[]; and 
    - adding the same to an empty list (i.e., Voter_ID_count) to get a count of votes by each candidate. 
