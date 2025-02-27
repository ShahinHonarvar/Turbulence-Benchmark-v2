import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = (matrix.shape[0], matrix.shape[1])
    result = []

    def check_submatrix(r1, c1, r2, c2):
        submatrix_sum = np.sum(matrix[r1:r2, c1:c2])
        return submatrix_sum == 56
    for size in range(1, min(rows, cols) + 1):
        for r1 in range(rows - size + 1):
            for c1 in range(cols - size + 1):
                for r2 in range(r1 + size, rows + 1):
                    for c2 in range(c1 + size, cols + 1):
                        if check_submatrix(r1, c1, r2, c2):
                            result.append(matrix[r1:r2, c1:c2])
    return result