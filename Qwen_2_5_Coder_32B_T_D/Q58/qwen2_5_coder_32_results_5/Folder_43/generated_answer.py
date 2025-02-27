import numpy as np

def submatrix_with_n_numbers(matrix):
    target = 85
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for m in range(i, rows):
                for n in range(j, cols):
                    if (m - i + 1) * (n - j + 1) == target:
                        if np.sum(matrix[i:m + 1, j:n + 1]) == target:
                            count += 1
    return count