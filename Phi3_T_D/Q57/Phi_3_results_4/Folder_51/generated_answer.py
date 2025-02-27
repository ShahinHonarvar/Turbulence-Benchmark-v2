import numpy as np

def submatrix_with_particular_sum(matrix, target_sum=-46):

    def submatrices(rows, cols, cur_rows, submatrices):
        if cur_rows > rows:
            return
        if cur_rows == rows:
            submatrices.append(matrix[:cur_rows, :cols])
            return
        submatrices(rows, cols, cur_rows + 1, submatrices)
        submatrices(rows, cols, cur_rows, submatrices + [matrix[:cur_rows, :cols]])
    valid_submatrices = []
    for rows in range(1, matrix.shape[0] + 1):
        for cols in range(1, matrix.shape[1] + 1):
            submatrices(matrix.shape[0], matrix.shape[1], 0, [])
            for submatrix in submatrices:
                if submatrix.sum() == target_sum:
                    valid_submatrices.append(submatrix)
    return valid_submatrices