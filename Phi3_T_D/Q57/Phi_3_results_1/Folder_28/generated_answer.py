import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for r_size in range(1, rows + 1):
        for c_size in range(1, cols + 1):
            for i in range(rows - r_size + 1):
                for j in range(cols - c_size + 1):
                    submat = matrix[i:i + r_size, j:j + c_size]
                    if np.sum(submat) == 15:
                        result.append(submat)
    return result