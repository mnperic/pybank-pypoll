# Import modules and dependencies
import os
import csv

# Define variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Set and open file from file path
file_path = os.path.join('/Resources/election_data.csv')

# Set, open and read .csv file from file path
with open(file_path, newline='') as csvfile:

    # Set .csv delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Determine header row
    csv_header = next(csvfile)

    # Read each row after the header
    for row in csvreader:
        
        # Calculate total number of votes cast
        total_votes += 1
        
        # Calculate total number of votes each candidate won
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1
            
    # Calculate percentage of votes each candidate won
    khan_percent = khan_votes / total_votes
    correy_percent = correy_votes / total_votes
    li_percent = li_votes / total_votes
    otooley_percent = otooley_votes / total_votes
    
    # Calculate winner (based on popular vote)
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 

# Print
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Khan: {khan_percent:.3%}({khan_votes})")
print(f"Correy: {correy_percent:.3%}({correy_votes})")
print(f"Li: {li_percent:.3%}({li_votes})")
print(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")

# Specify output file path
output_file = os.path.join('/Users/minoperic/Data Analytics/Homework/python-challenge/PyPoll/Analysis/election_data_revised.text')

# Open file in "write" mode and specify file type
with open(output_file, 'w',) as txtfile:

# Write
    txtfile.write(f"PyPoll - Election Results\n")
    txtfile.write(f"\n")
    txtfile.write(f"Total Votes: {total_votes:,}\n")
    txtfile.write(f"\n")
    txtfile.write(f"Khan: {khan_percent:.2%} ({khan_votes:,})\n")
    txtfile.write(f"Correy: {correy_percent:.2%} ({correy_votes:,})\n")
    txtfile.write(f"Li: {li_percent:.2%} ({li_votes:,})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.2%} ({otooley_votes:,})\n")
    txtfile.write(f"\n")
    txtfile.write(f"Winner: {winner_name}\n")
