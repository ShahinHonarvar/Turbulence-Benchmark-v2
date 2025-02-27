import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(mat, target):
        row, col = (len(mat), len(mat[0]))
        result = []
        for start_row in range(row):
            for end_row in range(start_row, row):
                temp = [0] * col
                for r in range(start_row, end_row + 1):
                    for c in range(col):
                        temp[c] += mat[r][c]
                    if sum(temp) == target:
                        result.append(np.array(mat[start_row:end_row + 1]))
        return result
    return submatrix_sum(matrix, 59)