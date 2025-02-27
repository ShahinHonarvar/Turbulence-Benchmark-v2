import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(m, n):
        count = 0
        rows, cols = m.shape
        for i in range(rows):
            for j in range(cols):
                if (i + 1) * (j + 1) == n:
                    count += 1
                elif (rows - i) * (j + 1) < n or (cols - j) * (i + 1) < n:
                    continue
                else:
                    for r in range(i + 1, rows + 1):
                        for c in range(j + 1, cols + 1):
                            if (r - i) * (c - j) == n:
                                count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 23)