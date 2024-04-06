# Dependencies / Modules
import os
import csv
from datetime import datetime

# Lists to store data
dates = []
months = []
date_objects = []
profit_and_loss = []
loss = []
profit = []
cleaned = []
Daily_changes = []
averages = []

# Counters
total_loss = 0
total_profit = 0

# Set path for the input file, 'budget_data.csv'
input_path = os.path.join('Resources', 'budget_data.csv')

# Open, and read in, the input file; split the 'str' datatype data on commas
with open(input_path, 'r') as input_file:
    csv_reader = csv.reader(input_file, delimiter = ',')
    
# Store the header row
    csv_header = next(csv_reader)

# Loop through looking for dates (mmm-yy) provided in the first element of the input_file (opened in the computer's memory as csv_reader); and 
    # push the dates to an array -- dates[]
    for date_and_profit_loss in csv_reader: 
        dates.append(date_and_profit_loss[0])
    
        # splitting the month/year, to extract the month from the dataset and push to an array --months[]; 
        split_dates = date_and_profit_loss[0].split("-")
        months.append(split_dates[0])
        
        # push the Profit/Loss (which is provided as the second element of the input_file) as an 'int' datatype to an array called profit_and_loss[]
        profit_and_loss.append(int(date_and_profit_loss[1]))
                           
    for profit_or_loss in profit_and_loss:
        if profit_or_loss < 0:
            loss.append(profit_or_loss)
            total_loss += (profit_or_loss)
        else:
            profit.append(profit_or_loss)
            total_profit += (profit_or_loss)

    Total = total_profit + total_loss

    # parsing the date from its string data type into Python's datetime data type; and adding it into an array called date_objects
    for date_string in dates:     
        dates_str = str(date_string)         
        date_objects.append(datetime.strptime(dates_str, '%b-%y'))

# The cleaned[] is a collection of the input_file elements (with the "Profit/Loss" column's data type changed to 'int'), along with a date_objects element using the datetime data type (to be used for sorting below, given that the "Date" being a 'str' type cannot be used for sorting)        
cleaned = list(zip(dates, date_objects, profit_and_loss))

# Using the date_objects[] variable in datetime format, in order to be able to sort the dates listed in the input_file (i.e. budget_data.csv)
cleaned.sort(key=lambda x:x[1]) 
# (where x = date, date_object, profit_and_loss)

for daily_change_sorted in range((len(cleaned)-1)):
    Daily_changes.append((cleaned[(daily_change_sorted)+1][0],(cleaned[(daily_change_sorted)+1][2]) - (cleaned[daily_change_sorted][2])))

# Calculating average
for daily_change in Daily_changes:
    averages.append(daily_change[1])

# Using the max() built-in function to find the max daily change
max_change = max(Daily_changes, key=lambda x:x[1])

# Using the min() built-in function to find the min daily change
min_change = min(Daily_changes, key=lambda x:x[1])
    
print("Financial Analysis\n--------------------")
print("Total Months: " + str(len(months)))
print("Total: " + "$" + (str(Total)))
print(f"Average Change: ${sum(averages)/len(averages):.2f}")
print(f"Greatest Increase in Profits: {max_change[0]} (${max_change[1]})")
print(f"Greatest Decrease in Profits: {min_change[0]} (${min_change[1]})")

# Set path for the output file, 'results.txt')
output_path = os.path.join("analysis", "results.txt")

# Open the output file using "write" mode.  Hold the contents in a variable, results_file: create a header row and oyjer content for Analysis
with open(output_path, 'w') as results_file:
  
    # Create the first two row for a Table header        
    print('Financial Analysis', file=results_file)
    print('-------------------', file=results_file)
    print('Total Months: ' + str(len(months)), file=results_file)
    print("Total: " + "$" + str(Total), file=results_file)
    print(f"Average Change: ${sum(averages)/len(averages):.2f}", file=results_file)
    print(f"Greatest Increase in Profits: {max_change[0]} (${max_change[1]})", file=results_file)
    print(f"Greatest Decrease in Profits: {min_change[0]} (${min_change[1]})", file=results_file)