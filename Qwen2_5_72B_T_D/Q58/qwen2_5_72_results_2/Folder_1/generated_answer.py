import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submat, n=23):
        flat_submat = submat.flatten()
        return np.sum(flat_submat == n)
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for size in range(1, min(rows - i, cols - j) + 1):
                submat = matrix[i:i + size, j:j + size]
                if count_elements(submat) == 23:
                    count += 1
    return count