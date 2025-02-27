import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for size in range(rows - i, 0, -1):
                for k_row in range(i, i + size):
                    for k_col in range(j, j + size):
                        submatrix = matrix[i:k_row + 1, j:k_col + 1]
                        if np.sum(submatrix) == 95:
                            result.append(submatrix)
    return result