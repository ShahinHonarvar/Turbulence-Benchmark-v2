import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 131
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for m in range(i, rows):
                for n in range(j, cols):
                    if (m - i + 1) * (n - j + 1) == n:
                        if np.sum(matrix[i:m + 1, j:n + 1]) == 131:
                            count += 1
    return count