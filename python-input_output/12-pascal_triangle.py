#!/usr/bin/python3
"""
This module contains a function that generates Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generates a list of lists of integers representing Pascal's triangle of n.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list of list of int: The generated Pascal's triangle matrix,
        or an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) < n:
        prev_row = triangle[-1]
        # Every row starts with 1
        current_row = [1]

        # Calculate the middle values based on the previous row
        for i in range(len(prev_row) - 1):
            current_row.append(prev_row[i] + prev_row[i + 1])

        # Every row ends with 1
        current_row.append(1)
        triangle.append(current_row)

    return triangle
