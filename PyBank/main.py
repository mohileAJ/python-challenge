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
Daily_changes = []

# Counters
total_loss = 0
total_profit = 0
Daily_change_count = 0

# Set path for the input file, 'budget_data.csv')
input_path = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join("analysis", "result.csv")

# Open the input file
with open(input_path) as input_file:
    csv_reader = csv.reader(input_file, delimiter = ',')
    csv_header = next(input_file)

# Loop through looking for month in the first element of the input_file
    for row in csv_reader: 
        profit_and_loss.append(int(row[1].replace("'", "").replace(" ", "").replace(",", "")))
        print(type(profit_and_loss[-1]))
        dates.append(row[0])
        datetime_str = row[0]
        # parsing the date from its string data type into Python's datetime data type; and adding it into an array called date_objects 
        date_objects.append(datetime.strptime(datetime_str, '%b-%d'))
        print(type(date_objects[-1]))
        # splitting the date/month/year, to extract the month from the dataset
        split_dates = row[0].split("-")
        months.append(split_dates[0])
    # print(type(row[1]))
    # print(type(row[0]))
    # print(profit_and_loss)

with open(input_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter = ',')
    csvheader = next(csv_file)
    # print(csvreader)
    for amt_row in csvreader:
        if "-" in row[1]:
            loss.append(int(amt_row[1].replace("'", "").replace(",", "")))
            total_loss += (int(amt_row[1].replace("'", "").replace(",", "")))
        else:
            profit.append(int(amt_row[1].replace("'", "").replace(",", "")))
            total_profit += (int(amt_row[1].replace(" ", "").replace(",", "")))

    Total = total_profit - total_loss
    print(type(Total))
    print(type(total_profit))
    # print(Total)

cleaned_amts_and_dates = list(zip(dates, date_objects, profit_and_loss))
# print(type([-1]))
# print(type(row[1]))

cleaned_amts_and_dates.sort(key=lambda x:x[1]) 
# (date, date_object, profit_and_loss)
# print(cleaned_amts_and_dates)

# Set path for the output file, 'results.csv')
output_path = os.path.join("analysis", "result.csv")

# Open the output file using "write" mode.  Hold the contents in a variable, results_file: , create a header row
#With open(output_path, 'w', newline='') as results_file:
    #csvwriter = csv.writer(results_file, delimiter = ',')
    
    # Create the first row for a Table header        
    #csvwriter.writerow('Financial Analysis')
    #csvwriter.writerow('-------------------')
    #csvwriter.writerow('Total Months: ' + str(len(months)))

# For i in range(len(cleaned_amts_and_dates)):
    # Daily_change_col

# print(profit_and_loss)
# print(row[0])
# print(months)
# print(type(row[0]))
        

    
print("Financial Analysis")
print("--------------------")
print("Total Months: " + str(len(months)))
print("Total: " + str(Total))
