import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_two_numbers(mat):
        rows, cols = mat.shape
        count = 0
        for i in range(rows):
            for j in range(cols):
                for size in range(1, min(rows - i, cols - j) + 1):
                    submat = mat[i:i + size, j:j + size]
                    if np.unique(submat).size == 2:
                        count += 1
        return count
    return count_submatrices_with_two_numbers(matrix)