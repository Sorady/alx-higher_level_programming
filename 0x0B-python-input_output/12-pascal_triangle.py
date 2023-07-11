#!/usr/bin/python3
"""12-pascal_triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    pascaln = [[1]]
    for i in range(1, n):
        prev = pascaln[i-1]
        cur = [1]
        for j in range(len(prev)-1):
            cur.append(prev[j] + prev[j+1])
        cur.append(1)
        pascaln.append(cur)
    return pascaln
