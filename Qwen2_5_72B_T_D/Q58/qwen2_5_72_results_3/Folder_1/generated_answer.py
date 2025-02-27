import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submat, n=23):
        return np.sum(submat == n)
    total_count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for r in range(i + 1, rows + 1):
                for c in range(j + 1, cols + 1):
                    if count_elements(matrix[i:r, j:c], 23) == 23:
                        total_count += 1
    return total_count