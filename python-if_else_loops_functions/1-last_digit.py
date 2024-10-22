#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)  # This line should not change

# Get the last digit of the number
last_digit = abs(number) % 10  # Use abs to handle negative numbers

# Prepare the output message
output = f"Last digit of {number} is {last_digit}"

# Determine the message based on the last digit
if last_digit > 5:
    output += " and is greater than 5"
elif last_digit == 0:
    output += " and is 0"
else:  # This covers the case where last_digit is less than 6 and not 0
    output += " and is less than 6 and not 0"

# Print the final output followed by a newline
print(output)  # This automatically ends with a newline

