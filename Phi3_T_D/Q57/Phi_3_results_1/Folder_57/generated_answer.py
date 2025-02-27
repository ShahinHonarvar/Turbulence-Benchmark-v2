import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrixes(mat, tar_sum):
        rows, cols = mat.shape
        res = []
        for left in range(cols):
            for right in range(left, cols):
                sub_sum = [0] * rows
                for i in range(rows):
                    sub_sum[i] = sum(mat[i, left:right + 1])
                    if sub_sum[i] == tar_sum:
                        res.append(mat[i - rows + 1:i + 1])
        return res
    result = find_submatrixes(matrix, 13)
    return result