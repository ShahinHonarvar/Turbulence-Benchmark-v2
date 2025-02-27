import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submat, n):
        return np.sum(submat == n)
    m, n = matrix.shape
    count = 0
    for i in range(m - 5 + 1):
        for j in range(n - 10 + 1):
            if count_elements(matrix[i:i + 5, j:j + 10], 59) == 59:
                count += 1
    return count