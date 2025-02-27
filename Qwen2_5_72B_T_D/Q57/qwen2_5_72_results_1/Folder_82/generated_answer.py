import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices(mat):
        rows, cols = mat.shape
        for y in range(rows):
            for x in range(cols):
                for height in range(1, rows - y + 1):
                    for width in range(1, cols - x + 1):
                        yield mat[y:y + height, x:x + width]
    target_sum_submatrices = [submat for submat in all_submatrices(matrix) if submat.sum() == -27]
    return target_sum_submatrices