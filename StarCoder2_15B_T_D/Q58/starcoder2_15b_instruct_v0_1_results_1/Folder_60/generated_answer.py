import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, column_count = matrix.shape
    submatrix_count = 0
    for row_start in range(row_count - 2):
        for column_start in range(column_count - 2):
            submatrix = matrix[row_start:row_start + 3, column_start:column_start + 3]
            if np.sum(submatrix == 88) == 88:
                submatrix_count += 1
    return submatrix_count