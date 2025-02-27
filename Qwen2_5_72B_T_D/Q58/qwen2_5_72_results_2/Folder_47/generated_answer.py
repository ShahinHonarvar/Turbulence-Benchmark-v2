import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        count = 0
        rows, cols = mat.shape
        submatrix_size = int(n ** 0.5)
        for i in range(rows - submatrix_size + 1):
            for j in range(cols - submatrix_size + 1):
                if np.size(mat[i:i + submatrix_size, j:j + submatrix_size]) == n:
                    count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 90)