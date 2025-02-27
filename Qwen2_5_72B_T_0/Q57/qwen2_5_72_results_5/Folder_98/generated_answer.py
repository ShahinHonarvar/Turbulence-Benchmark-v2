import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum_zero(mat):
        row, col = (len(mat), len(mat[0]))
        result = []
        for start_row in range(row):
            for end_row in range(start_row, row):
                temp = [0] * col
                for r in range(start_row, end_row + 1):
                    for c in range(col):
                        temp[c] += mat[r][c]
                sum_map = {0: -1}
                current_sum = 0
                for c in range(col):
                    current_sum += temp[c]
                    if current_sum in sum_map:
                        for prev_col in range(sum_map[current_sum] + 1, c + 1):
                            result.append(mat[start_row:end_row + 1, prev_col:c + 1])
                    sum_map.setdefault(current_sum, c)
        return result
    return find_submatrices_with_sum_zero(matrix)