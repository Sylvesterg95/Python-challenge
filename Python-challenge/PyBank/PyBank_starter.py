# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyBank", "Resources", "budget_data.csv")
file_to_output = os.path.join("budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
previous_profit = 0
changes = []
greatest_increase = ("", 0)  # (month, amount)
greatest_decrease = ("", float("inf"))  # (month, amount)

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:
        # Track the total months
        total_months += 1
        
        # Track the net total
        profit = int(row[1])
        total_net += profit
        
        # Calculate the change in profit/losses
        if total_months > 1:  # Skip the first month for change calculation
            change = profit - previous_profit
            changes.append(change)

            # Calculate the greatest increase in profits
            if change > greatest_increase[1]:
                greatest_increase = (row[0], change)

            # Calculate the greatest decrease in losses
            if change < greatest_decrease[1]:
                greatest_decrease = (row[0], change)

        # Update previous profit for next iteration
        previous_profit = profit

# Calculate the average net change across the months
average_change = sum(changes) / len(changes) if changes else 0

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
