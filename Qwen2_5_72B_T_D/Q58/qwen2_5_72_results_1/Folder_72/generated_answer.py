import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(matrix, n=16):
        count = 0
        rows, cols = matrix.shape
        for i in range(rows - 3):
            for j in range(cols - 3):
                submatrix = matrix[i:i + 4, j:j + 4]
                if np.sum(submatrix == 1) == n:
                    count += 1
        return count
    return count_submatrices(matrix)