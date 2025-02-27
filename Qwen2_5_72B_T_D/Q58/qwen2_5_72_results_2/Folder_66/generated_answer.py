import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submatrix, element=42):
        return np.sum(submatrix == element)
    target_count = 42
    rows, cols = matrix.shape
    valid_submatrices = 0
    for i in range(rows):
        for j in range(cols):
            for r in range(i + 1, rows + 1):
                for c in range(j + 1, cols + 1):
                    if count_elements(matrix[i:r, j:c]) == target_count:
                        valid_submatrices += 1
    return valid_submatrices