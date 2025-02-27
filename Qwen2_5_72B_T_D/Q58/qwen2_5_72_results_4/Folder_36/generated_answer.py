import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size_kxk(mat, k):
        count = 0
        rows, cols = mat.shape
        for i in range(rows - k + 1):
            for j in range(cols - k + 1):
                if np.prod(mat[i:i + k, j:j + k].shape) == 131:
                    count += 1
        return count
    k = int(np.sqrt(131))
    if k * k != 131:
        k = 1
    return count_submatrices_of_size_kxk(matrix, k)