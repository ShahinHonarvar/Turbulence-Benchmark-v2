import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for sub_rows in range(1, rows + 1):
        for sub_cols in range(1, cols + 1):
            if sub_rows == sub_cols == 121:
                return count + 1
            count += sum((1 for i in range(rows - sub_rows + 1) for j in range(cols - sub_cols + 1) if np.sum(matrix[i:i + sub_rows, j:j + sub_cols]) == 121))
    return count