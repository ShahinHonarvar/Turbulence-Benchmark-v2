import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        return 0
    total_rows, total_cols = matrix.shape
    count = 0
    for i in range(total_rows):
        for j in range(total_cols):
            for k in range(i, total_rows):
                for l in range(j, total_cols):
                    if (k - i + 1) * (l - j + 1) == 95:
                        count += 1
    return count