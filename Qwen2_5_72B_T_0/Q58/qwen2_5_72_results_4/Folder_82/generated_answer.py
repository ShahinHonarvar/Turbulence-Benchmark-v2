import numpy as np

def submatrix_with_n_numbers(matrix):
    target_number = 99
    submatrix_count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == target_number:
                for r in range(i + 1, rows + 1):
                    for c in range(j + 1, cols + 1):
                        submatrix = matrix[i:r, j:c]
                        if np.sum(submatrix == target_number) == 99:
                            submatrix_count += 1
    return submatrix_count