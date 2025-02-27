import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    target_size = 180
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for row_end in range(i + 1, rows + 1):
                for col_end in range(j + 1, cols + 1):
                    if (row_end - i) * (col_end - j) == target_size:
                        count += 1
    return count