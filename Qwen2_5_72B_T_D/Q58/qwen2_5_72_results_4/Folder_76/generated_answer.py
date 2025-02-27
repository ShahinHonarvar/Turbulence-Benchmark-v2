import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n(m, n):
        count = 0
        rows, cols = m.shape
        for i in range(rows):
            for j in range(cols):
                if i + 13 < rows and j + 13 < cols:
                    submatrix = m[i:i + 14, j:j + 14]
                    if np.sum(submatrix == 159) == 159:
                        count += 1
        return count
    return count_submatrices_with_n(matrix, 159)