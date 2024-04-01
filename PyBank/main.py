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
dates2 = []
profits2 = []
Daily_changes = []
cleaned_amts_and_dates = []

# Counters
total_loss = 0
total_profit = 0


# Set path for the input file, 'budget_data.csv')
input_path = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join("analysis", "result.csv")

# Open, and read in, the input file; split the str type data on commas
with open(input_path, 'r') as input_file:
    csv_reader = csv.reader(input_file, delimiter = ',')
    csv_header = next(csv_reader)

# Loop through looking for month in the first element of the input_file, and push to an array -- dates[]
    for date_and_profit_loss in csv_reader: 
        dates.append(date_and_profit_loss[0])
        dates_str = date_and_profit_loss[0]
        # parsing the date from its string data type into Python's datetime data type; and adding it into an array called date_objects 
        date_objects.append(datetime.strptime(dates_str, '%b-%y'))
        # print(type(date_objects[-1]))
        # splitting the date/month/year, to extract the month from the dataset
        split_dates = date_and_profit_loss[0].split("-")
        months.append(split_dates[0])
        profit_and_loss.append(int(date_and_profit_loss[1].replace("'", "").replace(" ", "").replace(",", "")))
        # print(type(profit_and_loss[-1]))
        
    # print(type(date_and_profit_loss[1]))
    # print(type(date_and_profit_loss[0]))
    # print(profit_and_loss)

        if "-" in date_and_profit_loss[1]:
            loss.append(int(date_and_profit_loss[1].replace("'", "").replace(",", "")))
            total_loss += (int(date_and_profit_loss[1].replace("'", "").replace(",", "")))
        else:
            profit.append(int(date_and_profit_loss[1].replace("'", "").replace(",", "")))
            total_profit += (int(date_and_profit_loss[1].replace(" ", "").replace(",", "")))

    Total = total_profit + total_loss
    # print(type(Total))
    # print(type(total_profit))
    # print(type(total_loss))
    # print(total_profit)
    # print(total_loss)    
    # print(Total)

cleaned = list(zip(dates, date_objects, profit_and_loss))
# print(type([-1]))
# print(type(row[1]))

cleaned.sort(key=lambda x:x[1]) 
# (where x = date, date_object, profit_and_loss)
# print(type(cleaned))

# for x in cleaned:
#     dates2.append(x[0])
#     profits2.append(x[2])
# zipped_profits = list(zip(dates2, profits2))
# # print(zipped_profits)
# print(type(profits2[1]))

for i in range((len(cleaned)-1)):
    # Daily_changes.append(zipped_profits[i+1][0])
    Daily_changes.append((cleaned[i+1][0],(cleaned[i+1][2]) - (cleaned[i][2])))
print(Daily_changes)

# Calculating average
averages = []
for item in Daily_changes:
    averages.append(item[1])
print((averages))
print(len(averages))


max_change = max(Daily_changes, key=lambda x:x[1])
# print(max_change)

min_change = min(Daily_changes, key=lambda x:x[1])
# print(min_change)

# print(profit_and_loss)
# print(row[0])
# print(months)
# print(type(row[0]))
        

    
print("Financial Analysis\n--------------------")
print("Total Months: " + str(len(months)))
print("Total: " + str(Total))
print(f"Average Change: ${sum(averages)/len(averages):.2f}")
print(f"Greatest Increase in Profits: {max_change[0]} (${max_change[1]})")
print(f"Greatest Decrease in Profits: {min_change[0]} (${min_change[1]})")


# Set path for the output file, 'results.csv')
output_path = os.path.join("analysis", "result.txt")

# Open the output file using "write" mode.  Hold the contents in a variable, results_file: , create a header row
with open(output_path, 'w') as results_file:
  
    # Create the first two row for a Table header        
    print('Financial Analysis', file=results_file)
    print('-------------------', file=results_file)
    print('Total Months: ' + str(len(months)), file=results_file)
    print("Total: " + str(Total), file=results_file)
    print(f"Average Change: ${sum(averages)/len(averages):.2f}", file=results_file)
    print(f"Greatest Increase in Profits: {max_change[0]} (${max_change[1]})", file=results_file)
    print(f"Greatest Decrease in Profits: {min_change[0]} (${min_change[1]})", file=results_file)
