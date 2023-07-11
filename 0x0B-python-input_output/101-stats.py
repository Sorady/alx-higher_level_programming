#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""
import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_count = {code: 0 for code in status_codes}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        data = line.split()
        try:
            status_code = int(data[-2])
            if status_code in status_codes:
                status_count[status_code] += 1
            total_size += int(data[-1])
        except:
            pass
        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_codes):
                if status_count[code]:
                    print("{}: {}".format(code, status_count[code]))
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_count[code]:
            print("{}: {}".format(code, status_count[code]))
