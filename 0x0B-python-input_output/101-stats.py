#!/usr/bin/python3
"""script to read stdin line by line and compute metrics"""

import sys  # Import the sys module to access stdin
import signal  # Import the signal module to handle keyboard interruption

# Initialize a dictionary to store the status codes and their counts
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
# Initialize a variable to store the total file size
total_size = 0
# Initialize a variable to store the number of lines read
line_count = 0

# Define a function to print the statistics


def print_stats():
    """Prints the statistics"""

    # Print the total file size
    print("File size: {}".format(total_size))
    # Loop through the status codes in ascending order
    for code in sorted(status_codes.keys()):
        # If the count is not zero, print the code and the count
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))

# Define a function to handle keyboard interruption


def signal_handler(sig, frame):
    """Handles keyboard interruption"""
    # Print the statistics before exiting
    print_stats()
    sys.exit(0)

# Register the signal handler for SIGINT (CTRL + C)


signal.signal(signal.SIGINT, signal_handler)

# Loop through each line in stdin
for line in sys.stdin:
    # Split the line by spaces
    tokens = line.split()
    # If the tokens are not empty
    if tokens:
        # Increment the line count
        line_count += 1
        # Try to get the status code and the file size from the last two tokens
        try:
            status_code = tokens[-2]
            file_size = int(tokens[-1])
            # Add the file size to the total size
            total_size += file_size
            # If the status code is in the dictionary, increment its count
            if status_code in status_codes:
                status_codes[status_code] += 1
        except Exception:
            # Ignore any exception and continue
            pass
    # If the line count is a multiple of 10, print the statistics
    if line_count % 10 == 0:
        print_stats()

# Print the statistics at the end of the loop
print_stats()
