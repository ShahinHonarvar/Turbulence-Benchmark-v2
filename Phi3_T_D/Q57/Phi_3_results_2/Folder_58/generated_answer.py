import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_all_submatrices(matrix, target_sum, i_min=0, j_min=0):
        nrows, ncols = matrix.shape
        submatrices = []
        for i in range(i_min, nrows):
            row_sum = 0
            for j in range(j_min, ncols):
                row_sum += matrix[i][j]
                for k in range(i, i + 2):
                    for l in range(j, j + 2):
                        if k < nrows and l < ncols:
                            submatrix_sum = 0
                            for x in range(i, min(nrows, i + 2)):
                                for y in range(j, min(ncols, j + 2)):
                                    submatrix_sum += matrix[x][y]
                            if submatrix_sum == target_sum:
                                submatrices.append(matrix[i:min(nrows, i + 2), j:min(ncols, j + 2)])
        return submatrices
    all_subs = find_all_submatrices(matrix, -137)
    return all_subs