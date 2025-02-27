import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submatrix, target_count):
        return np.sum(submatrix == target_count)
    target_count = 43
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for size in range(1, min(rows - i, cols - j) + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if count_elements(submatrix, target_count) == 43:
                    count += 1
    return count