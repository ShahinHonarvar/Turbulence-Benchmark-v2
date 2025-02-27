import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(m, n):
        count = 0
        for i in range(len(m) - 2):
            for j in range(len(m[0]) - 2):
                if np.sum(m[i:i + 3, j:j + 3] == n) == 8:
                    count += 1
        return count
    return count_submatrices(matrix, 8)