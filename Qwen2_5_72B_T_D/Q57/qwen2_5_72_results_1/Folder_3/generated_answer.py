import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum):
        row, col = mat.shape
        result = []
        for left in range(col):
            temp_sum = [0] * row
            for right in range(left, col):
                for i in range(row):
                    temp_sum[i] += mat[i][right]
                for top in range(row):
                    current_sum = 0
                    for bottom in range(top, row):
                        current_sum += temp_sum[bottom]
                        if current_sum == target_sum:
                            result.append(mat[top:bottom + 1, left:right + 1])
        return result
    return find_submatrices_with_sum(np.array(matrix), 54)