import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def check_submatrix(r1, c1, r2, c2):
        return np.sum(matrix[r1:r2 + 1, c1:c2 + 1]) == -15
    for size in range(1, rows + 1):
        for top in range(rows - size + 1):
            for left in range(cols - size + 1):
                if check_submatrix(top, left, top + size - 1, left + size - 1):
                    result.append(matrix[top:top + size, left:left + size])
    return result