import numpy as np

def submatrix_with_n_numbers(matrix):
    total_count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 104:
                for sub_rows in range(1, rows - i + 1):
                    for sub_cols in range(1, cols - j + 1):
                        submatrix = matrix[i:i + sub_rows, j:j + sub_cols]
                        if np.all(submatrix == 104):
                            total_count += 1
    return total_count