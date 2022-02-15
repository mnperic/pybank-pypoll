# Import dependencies
import os
import csv

# Determine variables
total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# File path
csvpath = os.path.join('.', 'PyBank', 'Resources', 'budget_data.csv')

    # Open/read .csv
    with open(csvpath, newline='') as csvfile:
    
    # Determine delimiter & variable for .csv
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Determine header row
    csv_header = next(csvreader)
    row = next(csvreader)
    
    # Determining total number of months, Profit/Loss amounts & variables for Rows
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    # Read each row
    for row in csvreader:
        
        # Total number of months
        total_months += 1
        # Profit/Loss net amount across entire period
        net_amount += int(row[1])

        # Change from current month to previous month
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        # Greatest increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        # Greatest decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
    # Average & date
    average_change = sum(monthly_change)/ len(monthly_change)
    
    highest = max(monthly_change)
    lowest = min(monthly_change)

# Print
print(f"Summary")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")

# File writing
output_file = os.path.join('.', 'PyBank', 'Resources', 'budget_data_revised.text')

# Open file ("write mode")
with open(output_file, 'w',) as txtfile:

# Printing new data
    txtfile.write(f"Summary\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_amount}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")