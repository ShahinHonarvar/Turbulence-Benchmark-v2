import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    target_count = 186
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if (rows - i) * (cols - j) >= target_count:
                for r in range(i + 1, rows + 1):
                    for c in range(j + 1, cols + 1):
                        if (r - i) * (c - j) == target_count:
                            count += 1
    return count