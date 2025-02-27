import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(m, target_size):
        rows, cols = m.shape
        count = 0
        for i in range(rows - target_size + 1):
            for j in range(cols - target_size + 1):
                if np.size(m[i:i + target_size, j:j + target_size]) == target_size:
                    count += 1
        return count
    return count_submatrices(matrix, 84)