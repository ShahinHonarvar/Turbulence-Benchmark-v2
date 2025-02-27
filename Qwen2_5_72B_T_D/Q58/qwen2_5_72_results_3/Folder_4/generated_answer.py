import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(m, n):
        count = 0
        rows, cols = m.shape
        for i in range(rows):
            for j in range(cols):
                if i + 3 <= rows and j + 5 <= cols and (np.size(m[i:i + 3, j:j + 5]) == n):
                    count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 15)