import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(m, n):
        rows, cols = m.shape
        count = 0
        for i in range(rows):
            for j in range(cols):
                for width in range(1, cols - j + 1):
                    for height in range(1, rows - i + 1):
                        if width * height == n:
                            if np.sum(m[i:i + height, j:j + width].size) == n:
                                count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 122)