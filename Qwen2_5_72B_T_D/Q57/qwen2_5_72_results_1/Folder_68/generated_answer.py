import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(mat, target_sum):
        row, col = (len(mat), len(mat[0]))
        result = []
        for top in range(row):
            for left in range(col):
                for bottom in range(top + 1, row + 1):
                    for right in range(left + 1, col + 1):
                        current_sum = np.sum(mat[top:bottom, left:right])
                        if current_sum == target_sum:
                            result.append(mat[top:bottom, left:right].tolist())
        return result
    return submatrix_sum(matrix, 3)