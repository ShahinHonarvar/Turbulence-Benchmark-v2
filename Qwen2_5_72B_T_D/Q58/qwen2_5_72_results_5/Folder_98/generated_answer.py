import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(m):
        count = 0
        rows, cols = m.shape
        for i in range(rows - 2):
            for j in range(cols - 2):
                if np.size(m[i:i + 3, j:j + 3]) == 9:
                    count += 1
        return count
    return count_submatrices(matrix)