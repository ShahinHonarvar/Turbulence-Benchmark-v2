import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submat, target=47):
        flat_list = submat.flatten()
        return np.count_nonzero(flat_list == target)
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            for size in range(1, min(m - i, n - j) + 1):
                submat = matrix[i:i + size, j:j + size]
                if count_elements(submat) == 47:
                    count += 1
    return count