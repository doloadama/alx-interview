#!/usr/bin/env python3
import sys

# Initialize variables to keep track of metrics
file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
num_lines = 0

# Read input line by line
for line in sys.stdin:
    try:
        # Extract the file size and status code from the line
        fields = line.strip().split()
        if len(fields) == 7:
            status_code = int(fields[5])
            if status_code in status_codes:
                file_size += int(fields[6])
                status_codes[status_code] += 1
                num_lines += 1
    except ValueError:
        pass

    # Print metrics after every 10 lines or keyboard interruption
    if num_lines % 10 == 0:
        print("Total file size:", file_size)
        for code in sorted(status_codes.keys()):
            if status_codes[code] > 0:
                print("{}: {}".format(code, status_codes[code]))

# Print final metrics after all input has been processed
print("Total file size:", file_size)
for code in sorted(status_codes.keys()):
    if status_codes[code] > 0:
        print("{}: {}".format(code, status_codes[code]))
