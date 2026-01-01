#!/usr/bin/python3
"""Defines a function that returns a list of lists of integers
 representing the Pascal's triangle of n."""


def pascal_triangle(n):
    """Returns a list of lists of integers
 representing the Pascal's triangle of n."""

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        curr_row = [1]

        for j in range(len(prev_row) - 1):
            curr_row.append(prev_row[j] + prev_row[j+1])
        curr_row.append(1)
        triangle.append(curr_row)

    return triangle
