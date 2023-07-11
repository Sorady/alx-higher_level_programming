#!/usr/bin/python3
import sys

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        tokens = line.split()
        total_size += int(tokens[-1])
        try:
            status_codes[int(tokens[-2])] += 1
        except KeyError:
            pass
        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for k in sorted(status_codes.keys()):
                if status_codes[k] != 0:
                    print("{}: {}".format(k, status_codes[k]))
        sys.stdout.flush()

except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for k in sorted(status_codes.keys()):
        if status_codes[k] != 0:
            print("{}: {}".format(k, status_codes[k]))
