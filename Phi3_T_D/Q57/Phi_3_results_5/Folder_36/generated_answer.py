import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices(matrix):
        rows, cols = matrix.shape
        for r_idx in range(rows):
            for c_idx in range(cols):
                for r_end in range(r_idx + 1, rows + 1):
                    for c_end in range(c_idx + 1, cols + 1):
                        yield matrix[r_idx:r_end, c_idx:c_end]
    result = []
    for submat in all_submatrices(matrix):
        if submat.sum() == -779:
            result.append(submat)
    return result