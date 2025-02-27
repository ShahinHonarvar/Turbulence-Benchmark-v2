import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count_69 = 0
    for size_x in range(1, m + 1):
        for size_y in range(1, n + 1):
            for i in range(m - size_x + 1):
                for j in range(n - size_y + 1):
                    submatrix = matrix[i:i + size_x, j:j + size_y]
                    if submatrix.size == 69:
                        count_69 += 1
    return count_69