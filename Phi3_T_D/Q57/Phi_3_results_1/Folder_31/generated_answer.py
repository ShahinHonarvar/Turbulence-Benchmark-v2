import numpy as np

def submatrix_with_particular_sum(mat):
    nrows, ncols = mat.shape
    sum_target = -44
    submatrices = []
    for i in range(nrows):
        for j in range(ncols):
            for k in range(i, nrows):
                for l in range(j, ncols):
                    sub_mat = mat[i:k + 1, j:l + 1]
                    if np.sum(sub_mat) == sum_target:
                        submatrices.append(sub_mat)
    return submatrices