import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 131
    if rows * cols < n:
        return 0
    result = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    if (k - i + 1) * (l - j + 1) == n:
                        if all((matrix[x][y] for x in range(i, k + 1) for y in range(j, l + 1))):
                            result += 1
    return result