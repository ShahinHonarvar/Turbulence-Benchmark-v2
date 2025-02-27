import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(matrix, k):
        rows, cols = matrix.shape
        count = 0
        for i in range(rows):
            for j in range(cols):
                for x in range(i, rows):
                    for y in range(j, cols):
                        if np.sum(matrix[i:x + 1, j:y + 1]) == k:
                            count += 1
        return count
    return count_submatrices(matrix, 83)