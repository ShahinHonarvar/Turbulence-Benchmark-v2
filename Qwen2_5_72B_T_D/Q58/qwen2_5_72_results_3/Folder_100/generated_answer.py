import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        count = 0
        rows, cols = mat.shape
        if n > rows * cols:
            return 0
        for i in range(rows):
            for j in range(cols):
                if (i + 1) * (j + 1) == n:
                    count += 1
                elif (rows - i) * (cols - j) >= n:
                    for end_i in range(i + 1, rows + 1):
                        for end_j in range(j + 1, cols + 1):
                            if (end_i - i) * (end_j - j) == n:
                                count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 10)