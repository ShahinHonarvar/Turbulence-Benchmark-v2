import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(n):
        count = 0
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if i + 6 < matrix.shape[0] and j + 6 < matrix.shape[1]:
                    submatrix = matrix[i:i + 7, j:j + 7]
                    if np.all(submatrix == 76):
                        count += 1
        return count
    return count_submatrices(76)