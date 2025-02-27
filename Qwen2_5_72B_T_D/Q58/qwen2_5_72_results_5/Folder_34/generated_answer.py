import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n(matrix, n):
        count = 0
        rows, cols = matrix.shape
        for i in range(rows):
            for j in range(cols):
                if i + 9 <= rows and j + 9 <= cols:
                    submatrix = matrix[i:i + 9, j:j + 9]
                    if np.sum(submatrix == n) == 83:
                        count += 1
        return count
    return count_submatrices_with_n(matrix, 83)