import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submat, n=38):
        return np.sum(submat == n)
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for r in range(i + 1, rows + 1):
                for c in range(j + 1, cols + 1):
                    if count_elements(matrix[i:r, j:c]) == 38:
                        count += 1
    return count