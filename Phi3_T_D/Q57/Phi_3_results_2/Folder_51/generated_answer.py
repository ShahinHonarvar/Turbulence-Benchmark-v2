import numpy as np

def submatrix_with_particular_sum(matrix):

    def check_submatrix(tl, br):
        return np.sum(matrix[tl[0]:br[0] + 1, tl[1]:br[1] + 1]) == -46

    def get_submatrices(row_start, row_end, col_start, col_end):
        result = []
        for i in range(row_start, row_end + 1):
            for j in range(col_start, col_end + 1):
                for k in range(i, row_end + 1):
                    for l in range(j, col_end + 1):
                        if check_submatrix((i, j), (k, l)):
                            result.append(matrix[i:k + 1, j:l + 1].tolist())
        return result
    result = []
    row_count, col_count = matrix.shape
    for r1 in range(row_count):
        for r2 in range(r1, row_count):
            for c1 in range(col_count):
                for c2 in range(c1, col_count):
                    result += get_submatrices(r1, r2, c1, c2)
    return result