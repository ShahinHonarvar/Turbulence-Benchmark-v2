import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 34

    def count_elements(submatrix, target_count):
        return np.sum(submatrix == target_count)
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for r in range(i + 1, rows + 1):
                for c in range(j + 1, cols + 1):
                    if count_elements(matrix[i:r, j:c], target_count) == target_count:
                        count += 1
    return count