#!/usr/bin/python3
import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
code_count = {code: 0 for code in status_codes}
total_size = 0
line_count = 0

def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(code_count.keys()):
        if code_count[code]:
            print("{}: {}".format(code, code_count[code]))

try:
    for line in sys.stdin:
        line_count += 1
        data = line.split()
        try:
            status_code = int(data[-2])
            file_size = int(data[-1])
            total_size += file_size
            if status_code in status_codes:
                code_count[status_code] += 1
        except:
            pass
        if line_count % 10 == 0:
            print_stats()
    print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
