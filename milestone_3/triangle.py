from typing import List
import sys


def get_triangle(rows: int) -> List[List[int]]:
    for i in range(1, rows + 1):
        for j in range(0, rows - i + 1):
            print(' ', end='')
        C = 1
        for j in range(1, i + 1):
            print(' ', C, sep='', end='')
            # using Binomial Coefficient
            C = C * (i - j) // j
        print()


# add command-line argument: python triangle.py 5
if len(sys.argv) != 2:
    print("Usage: python triangle.py <number_of_rows>")
else:
    try:
        rows = int(sys.argv[1])
        get_triangle(rows)
    except ValueError:
        print("Please enter a valid integer for the number of rows.")