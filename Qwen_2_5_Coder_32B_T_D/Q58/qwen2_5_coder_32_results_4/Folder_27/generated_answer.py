import numpy as np

def submatrix_with_n_numbers(matrix):
    count, n = (0, 77)
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for x in range(i, rows):
                for y in range(j, cols):
                    if (x - i + 1) * (y - j + 1) == n:
                        if np.sum(matrix[i:x + 1, j:y + 1]) == n:
                            count += 1
    return count