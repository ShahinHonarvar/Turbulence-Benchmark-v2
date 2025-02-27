import numpy as np

def submatrix_with_particular_sum(matrix):
    if matrix.size == 0:
        return []
    rows, cols = matrix.shape
    result = []
    for sr in range(rows):
        for sc in range(cols):
            for er in range(sr, rows):
                for ec in range(sc, cols):
                    sub_matrix = matrix[sr:er + 1, sc:ec + 1]
                    if np.sum(sub_matrix) == 64:
                        result.append(sub_matrix)
    return result