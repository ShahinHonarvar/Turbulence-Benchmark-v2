import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 191
    if len(matrix) <= n or len(matrix[0]) <= n:
        return 0
    count = 0
    rows, cols = (len(matrix), len(matrix[0]))
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            flattened = submatrix.flatten()
            group_indices = np.arange(len(flattened)) // n
            if len(set(group_indices)) == n:
                count += 1
    return count