import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size_kxk(matrix, k, required_count):
        rows, cols = matrix.shape
        count = 0
        for i in range(rows - k + 1):
            for j in range(cols - k + 1):
                submatrix = matrix[i:i + k, j:j + k]
                if np.sum(submatrix == required_count) == required_count:
                    count += 1
        return count
    return count_submatrices_of_size_kxk(matrix, 6, 37)