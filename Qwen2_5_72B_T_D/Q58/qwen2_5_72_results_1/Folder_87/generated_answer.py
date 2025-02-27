import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(m, n):
        count = 0
        rows, cols = m.shape
        for i in range(rows):
            for j in range(cols):
                if i + 10 <= rows and j + 10 <= cols and (np.size(m[i:i + 10, j:j + 10]) == n):
                    count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 96)