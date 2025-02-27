import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 130

    def is_valid_submatrix(row, col, r, c):
        return row + r - 1 < rows and col + c - 1 < cols
    for row in range(rows):
        for col in range(cols):
            for r in range(1, rows - row + 1):
                for c in range(1, cols - col + 1):
                    if r * c == n and is_valid_submatrix(row, col, r, c):
                        count += 1
    return count