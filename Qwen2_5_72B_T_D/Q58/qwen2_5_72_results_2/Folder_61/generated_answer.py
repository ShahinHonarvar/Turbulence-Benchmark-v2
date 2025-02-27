import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_4(matrix):
        rows, cols = matrix.shape
        count = 0
        for i in range(rows - 1):
            for j in range(cols - 1):
                submatrix = matrix[i:i + 2, j:j + 2]
                if np.sum(submatrix > 0) == 4:
                    count += 1
        return count
    return count_submatrices_with_4(matrix)