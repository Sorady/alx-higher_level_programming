#!/usr/bin/python3
"""the queens gambit"""


import sys

def nqueens(n):
    def backtrack(queens, xy_dif, xy_sum):
        p = len(queens)
        if p == n:
            result.append(queens)
            return
        for q in range(n):
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                backtrack(queens+[q], xy_dif+[p-q], xy_sum+[p+q])

    result = []
    backtrack([],[],[])
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    solutions = nqueens(n)
    for solution in solutions:
        print([[i, solution[i]] for i in range(n)])
