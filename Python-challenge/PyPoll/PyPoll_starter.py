"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os


# Files to load and output (update with correct file paths)
file_to_load = os.path.join (r"C:\\Users\\sylve\\Desktop\\dataclass\\Python-challenge\\PyPoll\\Resources/election_data.csv")  # Input file path
file_to_output = os.path.join("C:\\Users\\sylve\\Desktop\\dataclass\\Python-challenge\\PyPoll\\Resources/election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_votes = {}
winning_count = 0
winning_candidate = ""

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]  # Assuming the candidate's name is in the third column

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0  # Initialize vote count for new candidate

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f"\nTotal Votes: {total_votes}")
    # Write the total vote count to the text file
    txt_file.write(f"Total Votes: {total_votes}\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
        txt_file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")

    # Generate and print the winning candidate summary
    winning_summary = f"Winner: {winning_candidate}\n"
    print(winning_summary)
    txt_file.write(winning_summary)