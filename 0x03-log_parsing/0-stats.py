#!/usr/bin/env python3

import sys

# Initialize variables
total_size = 0
status_codes = {}

# Define function to print metrics
def print_metrics():
    print("Total file size:", total_size)
    for code in sorted(status_codes):
        print(code, ":", status_codes[code])

# Read from stdin line by line
for i, line in enumerate(sys.stdin):
    try:
        # Parse line in the format <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
        ip, _, _, _, _, status_code, file_size = line.split()
        status_code = int(status_code)
        file_size = int(file_size)
        # Update metrics
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1
        # Print metrics every 10 lines
        if (i + 1) % 10 == 0:
            print_metrics()
    except ValueError:
        # Skip lines that don't match the format
        continue
    except KeyboardInterrupt:
        # Print metrics and exit on keyboard interruption
        print_metrics()
        sys.exit(0)

# Print final metrics
print_metrics()
