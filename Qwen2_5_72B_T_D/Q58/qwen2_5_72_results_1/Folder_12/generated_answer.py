import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(m, n=46):
        count = 0
        for i in range(m.shape[0] - 1):
            for j in range(m.shape[1] - 1):
                submatrix = m[i:i + 2, j:j + 2]
                if np.sum(submatrix) == n:
                    count += 1
        return count
    return count_submatrices_with_n_elements(matrix)