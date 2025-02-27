import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_target_sum(mat, target):
        rows, cols = mat.shape
        result = []
        for left in range(cols):
            temp = [0] * rows
            for right in range(left, cols):
                for i in range(rows):
                    temp[i] += mat[i][right]
                cum_sum = {0: -1}
                cur_sum = 0
                for i, val in enumerate(temp):
                    cur_sum += val
                    if cur_sum - target in cum_sum:
                        top = cum_sum[cur_sum - target] + 1
                        result.append(mat[top:i + 1, left:right + 1])
                    cum_sum[cur_sum] = i
        return result
    return find_submatrices_with_target_sum(np.array(matrix), -308)