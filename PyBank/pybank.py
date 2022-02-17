# Import modules and dependencies
import os
import csv

# Define variables
total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# Set and open file from file path
file_path = os.path.join('/Users/minoperic/Data Analytics/Homework/python-challenge/PyBank/Resources/budget_data.csv')

# Set, open and read .csv file from file path
with open(file_path, newline='') as csvfile:
    
    # Set .csv delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Determine header row
    csv_header = next(csvreader)
    row = next(csvreader)
    
    # Calculate total number of months, net amount of Profit/Losses and set row variables
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    # Read each row after the header
    for row in csvreader:
        
        # Calculate "Total Number Of Months"
        total_months += 1
        # Calculate "Net Amount Of 'Profit/Losses'"" across entire period"
        net_amount += int(row[1])

        # Calculate "Change From Current Month To Previous Month"
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        # Calculate "Greatest Increase"
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        # Calculate "Greatest Decrease"
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0] 

        # Calculate "difference betweeen Greatest Increase and Greatest Decrease"
        greatest_difference = greatest_increase - greatest_decrease 
        
    # Calculate "Average" and "Date"
    average_change = sum(monthly_change)/ len(monthly_change)
    
    highest = max(monthly_change)
    lowest = min(monthly_change)

# Print
print(f"Analysis")
print(f"")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month}, (${lowest})")
print(f"Difference/Range: ${greatest_difference}")

# Set output file path
output_file = os.path.join('/Users/minoperic/Data Analytics/Homework/python-challenge/PyBank/Analysis/budget_data_revised.text')

# Open file in "write" mode and specify file type
with open(output_file, 'w',) as txtfile:

# Write
    txtfile.write(f"PyBank - Summary Analysis\n")
    txtfile.write(f"\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"\n")
    txtfile.write(f"Total: ${net_amount:,}\n")
    txtfile.write(f"Average Change: ${average_change:,.2f}\n")
    txtfile.write(f"\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month}, (${highest:,})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month}, (${lowest:,})\n")
    txtfile.write(f"\n")
    txtfile.write(f"Difference/Range: (${greatest_difference:,})\n")