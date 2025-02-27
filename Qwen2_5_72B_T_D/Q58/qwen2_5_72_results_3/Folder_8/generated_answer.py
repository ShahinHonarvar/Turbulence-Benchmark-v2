import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submat, n=29):
        return np.sum(submat == n)
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for r in range(1, rows - i + 1):
                for c in range(1, cols - j + 1):
                    submat = matrix[i:i + r, j:j + c]
                    if count_elements(submat) == 29:
                        count += 1
    return count