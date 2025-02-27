import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size_kxk(matrix, k, target_count):
        count = 0
        rows, cols = matrix.shape
        if k * k != target_count or rows < k or cols < k:
            return 0
        for i in range(rows - k + 1):
            for j in range(cols - k + 1):
                submatrix = matrix[i:i + k, j:j + k]
                if submatrix.size == target_count:
                    count += 1
        return count
    return count_submatrices_of_size_kxk(matrix, int(np.sqrt(126)), 126)