import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    n = 29

    def is_valid_submatrix(x, y):
        return x < rows and y < cols and ((rows - x) * (cols - y) >= n)
    for i in range(rows):
        for j in range(cols):
            for r in range(i, rows):
                for c in range(j, cols):
                    if (r - i + 1) * (c - j + 1) == n:
                        count += 1
                    elif (r - i + 1) * (c - j + 1) > n:
                        break
    return count