import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(matrix, size):
        count = 0
        rows, cols = matrix.shape
        if size > rows * cols:
            return 0
        for i in range(rows - int(np.ceil(np.sqrt(size))) + 1):
            for j in range(cols - int(np.ceil(np.sqrt(size))) + 1):
                submatrix = matrix[i:i + int(np.ceil(np.sqrt(size))), j:j + int(np.ceil(np.sqrt(size)))]
                if np.product(submatrix.shape) == size:
                    count += 1
        return count
    return count_submatrices_of_size(matrix, 139)